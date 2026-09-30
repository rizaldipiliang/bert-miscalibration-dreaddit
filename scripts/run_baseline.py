import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.train import run_experiment

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--train", default="data/raw/dreaddit-train.csv")
    p.add_argument("--test", default="data/raw/dreaddit-test.csv")
    p.add_argument("--output_dir", default="results/run_seed42")
    p.add_argument("--text_col", default=None)
    p.add_argument("--label_col", default=None)
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()

    out = run_experiment(
        train_path=args.train,
        test_path=args.test,
        output_dir=args.output_dir,
        text_col=args.text_col,
        label_col=args.label_col,
        seed=args.seed,
    )
    print("Finished.")
    for k, v in out["metrics"].items():
        print(f"{k}: {v:.6f}")

if __name__ == "__main__":
    main()
