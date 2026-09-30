from pathlib import Path
import pandas as pd

paths = [
    Path("data/raw/dreaddit-train.csv"),
    Path("data/raw/dreaddit-test.csv"),
]
expected = {
    "dreaddit-train.csv": 2838,
    "dreaddit-test.csv": 715,
}

missing = [str(p) for p in paths if not p.exists()]
if missing:
    raise SystemExit(
        "Missing Dreaddit files:\n- " + "\n- ".join(missing) +
        "\nSee data/README.md for provenance and placement instructions."
    )

for p in paths:
    df = pd.read_csv(p)
    print(f"{p}: {len(df):,} rows; columns={list(df.columns)}")
    exp = expected[p.name]
    if len(df) != exp:
        print(
            f"  NOTE: article-reported count is {exp:,}. "
            "Do not silently modify the source; document the version you obtained."
        )
