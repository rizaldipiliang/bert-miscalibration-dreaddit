# Vanilla BERT Confidence Miscalibration on Dreaddit

[![Article DOI](https://img.shields.io/badge/Article_DOI-10.63158%2Fjournalisi.v8i3.1634-blue)](https://doi.org/10.63158/journalisi.v8i3.1634)
[![Python](https://img.shields.io/badge/Python-3.10%2B-informational)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/Code_License-MIT-green.svg)](LICENSE)
[![Reproducibility](https://img.shields.io/badge/reproducibility-baseline-orange)](#reproducibility-scope)

Reproducibility repository for:

> **Rizaldi, Kusrini, Ema Utami, and I Made Artha Agastya (2026).  
> “An Empirical Evaluation of Confidence Miscalibration in Vanilla BERT-Based Stress Detection on Social Media.”  
> Journal of Information Systems and Informatics, 8(3), 3014–3034.**  
> DOI: https://doi.org/10.63158/journalisi.v8i3.1634

## Why this repository exists

The article evaluates whether a competitive Vanilla BERT stress classifier also produces
reliable confidence estimates. The repository is designed to make the diagnostic baseline
easy to inspect, reproduce, cite, and extend toward calibration, uncertainty estimation,
distribution shift, and selective prediction research.

### Paper-reported baseline

| Metric | Reported value |
|---|---:|
| Accuracy | 0.7902 |
| Precision | 0.7800 |
| Recall | 0.8265 |
| F1-score | 0.8026 |
| Brier Score | 0.1565 |
| Expected Calibration Error (ECE, 10 equal-width bins) | 0.0847 |
| Adaptive Calibration Error (ACE, 10 equal-frequency bins) | 0.0880 |

### Paper-reported training configuration

| Parameter | Value |
|---|---|
| Base model | `bert-base-uncased` |
| Task | Binary stress classification |
| Max sequence length | 128 |
| Learning rate | 2e-5 |
| Train batch size | 16 |
| Evaluation batch size | 32 |
| Weight decay | 0.01 |
| Epochs | 3 |
| Loss | Cross-entropy |
| Random seed | 42 |
| Train split | 2,838 segments |
| Test split | 715 segments |

## Repository structure

```text
.
├── CITATION.cff
├── LICENSE
├── README.md
├── requirements.txt
├── environment.yml
├── pyproject.toml
├── .zenodo.json
├── data/
│   ├── README.md
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_reproduce_baseline.ipynb
├── scripts/
│   ├── check_data.py
│   └── run_baseline.py
├── src/
│   ├── __init__.py
│   ├── data_utils.py
│   ├── metrics.py
│   └── train.py
├── results/
│   └── paper_reported_metrics.json
├── figures/
│   └── .gitkeep
├── docs/
│   ├── DATASET.md
│   ├── REPRODUCIBILITY.md
│   ├── ZENODO_RELEASE_GUIDE.md
│   ├── PROMOTION_KIT.md
│   └── OUTREACH_TRACKER.csv
└── .github/
    └── workflows/
        └── smoke-test.yml
```

## Quick start

### 1. Create an environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

### 2. Obtain Dreaddit from the original source

This repository intentionally does **not** redistribute the raw Dreaddit files. See
[`data/README.md`](data/README.md) and [`docs/DATASET.md`](docs/DATASET.md).

Place the original files as:

```text
data/raw/dreaddit-train.csv
data/raw/dreaddit-test.csv
```

### 3. Validate the input files

```bash
python scripts/check_data.py
```

The paper used a total of 3,553 labeled segments, with 2,838 training and 715 test segments.
If the upstream copy you obtain differs slightly, preserve the official split and document
the exact source/version used.

### 4. Reproduce the baseline

```bash
python scripts/run_baseline.py \
  --train data/raw/dreaddit-train.csv \
  --test data/raw/dreaddit-test.csv \
  --output_dir results/run_seed42
```

The pipeline detects common Dreaddit column names automatically. You can explicitly set
`--text_col` and `--label_col` if needed.

### 5. Notebook workflow

Open:

```text
notebooks/01_reproduce_baseline.ipynb
```

It walks through data loading, fine-tuning, prediction export, classification metrics,
Brier Score, ECE, ACE, and the reliability diagram.

## Reproducibility scope

This package reconstructs the **paper-reported experimental protocol**. The article did not
report exact package versions, CUDA version, GPU model, or a frozen environment hash.
Therefore, the repository does not claim bit-for-bit reproduction of the original runtime.

The scientifically important fixed choices are preserved:

- standard Dreaddit train/test split;
- Vanilla `bert-base-uncased`;
- max length 128;
- learning rate 2e-5;
- train/eval batch sizes 16/32;
- weight decay 0.01;
- three epochs;
- seed 42;
- no post-hoc calibration or label smoothing in the baseline;
- ECE using 10 equal-width confidence bins;
- ACE using 10 equal-frequency confidence bins;
- Brier Score using the predicted probability of the positive (`Stress`) class.

## Expected output

A successful run writes:

```text
results/run_seed42/
├── metrics.json
├── predictions.csv
├── reliability_diagram.png
└── training_output/
```

Small numerical differences from the article may occur because of hardware, library,
tokenizer, and runtime differences. Record your environment when reporting a replication.

## Citation

If this repository or baseline is useful in your research, please cite the **article**
using the metadata in [`CITATION.cff`](CITATION.cff) or the BibTeX below.

```bibtex
@article{rizaldi2026confidence,
  title   = {An Empirical Evaluation of Confidence Miscalibration in Vanilla BERT-Based Stress Detection on Social Media},
  author  = {Rizaldi and Kusrini and Utami, Ema and Agastya, I Made Artha},
  journal = {Journal of Information Systems and Informatics},
  volume  = {8},
  number  = {3},
  pages   = {3014--3034},
  year    = {2026},
  month   = {6},
  doi     = {10.63158/journalisi.v8i3.1634},
  url     = {https://doi.org/10.63158/journalisi.v8i3.1634}
}
```

Please also cite the original Dreaddit dataset paper:

```bibtex
@inproceedings{turcan2019dreaddit,
  title     = {Dreaddit: A Reddit Dataset for Stress Analysis in Social Media},
  author    = {Turcan, Elsbeth and McKeown, Kathy},
  booktitle = {Proceedings of the Tenth International Workshop on Health Text Mining and Information Analysis},
  pages     = {97--107},
  year      = {2019},
  publisher = {Association for Computational Linguistics},
  doi       = {10.18653/v1/D19-6213}
}
```

## Extending this baseline

Natural next experiments include:

- temperature scaling;
- label smoothing;
- isotonic or Platt-style post-hoc calibration;
- deep ensembles / MC dropout;
- conformal prediction;
- calibration under temporal or domain shift;
- selective prediction / risk-coverage evaluation;
- high-confidence error analysis.

Keep any follow-up study scientifically distinct from the published baseline and cite prior
work only where it is genuinely relevant.

## Licensing

Code in this repository is released under the MIT License. The journal article is published
under CC BY 4.0 by the journal. Dreaddit is a third-party dataset: obtain it from its original
source and follow the dataset authors' terms. The dataset itself is not covered by this
repository's MIT License.
