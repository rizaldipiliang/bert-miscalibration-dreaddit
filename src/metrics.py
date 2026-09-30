from __future__ import annotations
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, brier_score_loss

def classification_metrics(y_true, y_pred):
    p, r, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="binary", pos_label=1, zero_division=0
    )
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(p),
        "recall": float(r),
        "f1": float(f1),
    }

def expected_calibration_error(y_true, probs, n_bins=10):
    """
    Paper-aligned ECE:
    - confidence = max class probability
    - correctness = predicted label == true label
    - 10 equal-width confidence bins by default
    """
    probs = np.asarray(probs, dtype=float)
    y_true = np.asarray(y_true, dtype=int)
    pred = probs.argmax(axis=1)
    conf = probs.max(axis=1)
    correct = (pred == y_true).astype(float)

    edges = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    rows = []
    n = len(y_true)

    for i in range(n_bins):
        lo, hi = edges[i], edges[i + 1]
        mask = (conf >= lo) & (conf < hi if i < n_bins - 1 else conf <= hi)
        count = int(mask.sum())
        if count == 0:
            rows.append({
                "bin": i + 1, "lower": float(lo), "upper": float(hi),
                "count": 0, "accuracy": None, "confidence": None, "gap": None
            })
            continue
        acc = float(correct[mask].mean())
        avg_conf = float(conf[mask].mean())
        gap = abs(acc - avg_conf)
        ece += (count / n) * gap
        rows.append({
            "bin": i + 1, "lower": float(lo), "upper": float(hi),
            "count": count, "accuracy": acc, "confidence": avg_conf, "gap": float(gap)
        })
    return float(ece), rows

def adaptive_calibration_error(y_true, probs, n_bins=10):
    """
    Paper-aligned ACE using equal-frequency bins after sorting by prediction confidence.
    Returns the unweighted mean absolute confidence-accuracy gap over non-empty bins.
    """
    probs = np.asarray(probs, dtype=float)
    y_true = np.asarray(y_true, dtype=int)
    pred = probs.argmax(axis=1)
    conf = probs.max(axis=1)
    correct = (pred == y_true).astype(float)

    order = np.argsort(conf)
    groups = np.array_split(order, n_bins)

    gaps, rows = [], []
    for i, idx in enumerate(groups, start=1):
        if len(idx) == 0:
            continue
        acc = float(correct[idx].mean())
        avg_conf = float(conf[idx].mean())
        gap = abs(acc - avg_conf)
        gaps.append(gap)
        rows.append({
            "bin": i,
            "count": int(len(idx)),
            "accuracy": acc,
            "confidence": avg_conf,
            "gap": float(gap)
        })
    return float(np.mean(gaps)), rows

def brier_positive_class(y_true, probs):
    """
    Binary Brier Score using P(Stress=1), matching the article description.
    """
    probs = np.asarray(probs, dtype=float)
    y_true = np.asarray(y_true, dtype=int)
    return float(brier_score_loss(y_true, probs[:, 1]))

def all_metrics(y_true, probs, n_bins=10):
    probs = np.asarray(probs, dtype=float)
    pred = probs.argmax(axis=1)
    m = classification_metrics(y_true, pred)
    ece, ece_bins = expected_calibration_error(y_true, probs, n_bins=n_bins)
    ace, ace_bins = adaptive_calibration_error(y_true, probs, n_bins=n_bins)
    m.update({
        "brier_score": brier_positive_class(y_true, probs),
        "ece": ece,
        "ace": ace
    })
    return m, ece_bins, ace_bins
