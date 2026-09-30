from __future__ import annotations
import json
import os
import random
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from datasets import Dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)

from .data_utils import load_split
from .metrics import all_metrics

def set_seed_everywhere(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

def _softmax(logits):
    z = logits - logits.max(axis=1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=1, keepdims=True)

def run_experiment(
    train_path,
    test_path,
    output_dir,
    text_col=None,
    label_col=None,
    model_name="bert-base-uncased",
    max_length=128,
    learning_rate=2e-5,
    train_batch_size=16,
    eval_batch_size=32,
    weight_decay=0.01,
    epochs=3,
    seed=42,
    n_bins=10,
):
    set_seed_everywhere(seed)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    train_df = load_split(train_path, text_col=text_col, label_col=label_col)
    test_df = load_split(test_path, text_col=text_col, label_col=label_col)

    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

    def tokenize(batch):
        return tokenizer(
            batch["text"],
            padding="max_length",
            truncation=True,
            max_length=max_length,
        )

    train_ds = Dataset.from_pandas(train_df, preserve_index=False).map(tokenize, batched=True)
    test_ds = Dataset.from_pandas(test_df, preserve_index=False).map(tokenize, batched=True)

    train_ds = train_ds.rename_column("label", "labels")
    test_ds = test_ds.rename_column("label", "labels")
    cols = ["input_ids", "attention_mask", "labels"]
    train_ds.set_format(type="torch", columns=cols)
    test_ds.set_format(type="torch", columns=cols)

    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

    args = TrainingArguments(
        output_dir=str(output_dir / "training_output"),
        learning_rate=learning_rate,
        per_device_train_batch_size=train_batch_size,
        per_device_eval_batch_size=eval_batch_size,
        num_train_epochs=epochs,
        weight_decay=weight_decay,
        seed=seed,
        data_seed=seed,
        save_strategy="epoch",
        logging_strategy="epoch",
        report_to=[],
        load_best_model_at_end=False,
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_ds,
        eval_dataset=test_ds,
        tokenizer=tokenizer,
    )
    trainer.train()

    pred_out = trainer.predict(test_ds)
    probs = _softmax(pred_out.predictions)
    y_true = np.asarray(test_df["label"], dtype=int)
    y_pred = probs.argmax(axis=1)
    confidence = probs.max(axis=1)

    metrics, ece_bins, ace_bins = all_metrics(y_true, probs, n_bins=n_bins)

    pred_df = pd.DataFrame({
        "text": test_df["text"],
        "label": y_true,
        "predicted_label": y_pred,
        "prob_not_stress": probs[:, 0],
        "prob_stress": probs[:, 1],
        "confidence": confidence,
        "correct": (y_true == y_pred).astype(int),
    })
    pred_df.to_csv(output_dir / "predictions.csv", index=False)

    payload = {
        "configuration": {
            "model_name": model_name,
            "max_length": max_length,
            "learning_rate": learning_rate,
            "train_batch_size": train_batch_size,
            "eval_batch_size": eval_batch_size,
            "weight_decay": weight_decay,
            "epochs": epochs,
            "seed": seed,
            "n_bins": n_bins,
            "train_rows": int(len(train_df)),
            "test_rows": int(len(test_df)),
        },
        "metrics": metrics,
        "ece_bins": ece_bins,
        "ace_bins": ace_bins,
    }
    (output_dir / "metrics.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    # Reliability diagram
    import matplotlib.pyplot as plt
    xs, ys = [], []
    for row in ece_bins:
        if row["count"] > 0:
            xs.append(row["confidence"])
            ys.append(row["accuracy"])
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot([0, 1], [0, 1], linestyle="--", label="Perfect calibration")
    ax.plot(xs, ys, marker="o", label="Vanilla BERT")
    ax.set_xlabel("Mean confidence")
    ax.set_ylabel("Empirical accuracy")
    ax.set_title("Reliability Diagram")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "reliability_diagram.png", dpi=200)
    plt.close(fig)

    return payload
