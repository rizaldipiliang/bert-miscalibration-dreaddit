from __future__ import annotations
from pathlib import Path
import pandas as pd

TEXT_CANDIDATES = ["text", "sentence", "post", "body", "content"]
LABEL_CANDIDATES = ["label", "stress", "target", "class"]

def _resolve_column(columns, requested, candidates, kind):
    if requested:
        if requested not in columns:
            raise ValueError(f"{kind} column '{requested}' not found. Available: {list(columns)}")
        return requested
    lowered = {str(c).lower(): c for c in columns}
    for c in candidates:
        if c in lowered:
            return lowered[c]
    raise ValueError(
        f"Could not infer {kind} column. Pass --{kind}_col explicitly. "
        f"Available columns: {list(columns)}"
    )

def load_split(path, text_col=None, label_col=None):
    path = Path(path)
    df = pd.read_csv(path)
    text_col = _resolve_column(df.columns, text_col, TEXT_CANDIDATES, "text")
    label_col = _resolve_column(df.columns, label_col, LABEL_CANDIDATES, "label")

    out = df[[text_col, label_col]].copy()
    out.columns = ["text", "label"]
    out["text"] = out["text"].fillna("").astype(str)

    # Normalize common binary encodings.
    if out["label"].dtype == object:
        mapping = {
            "stress": 1, "stressed": 1, "1": 1, "true": 1,
            "not stress": 0, "not_stress": 0, "non-stress": 0,
            "0": 0, "false": 0
        }
        vals = out["label"].astype(str).str.strip().str.lower()
        mapped = vals.map(mapping)
        if mapped.isna().any():
            bad = sorted(vals[mapped.isna()].unique())[:10]
            raise ValueError(f"Unrecognized label values: {bad}")
        out["label"] = mapped.astype(int)
    else:
        out["label"] = out["label"].astype(int)

    bad_labels = set(out["label"].unique()) - {0, 1}
    if bad_labels:
        raise ValueError(f"Labels must be binary 0/1. Found: {bad_labels}")

    return out
