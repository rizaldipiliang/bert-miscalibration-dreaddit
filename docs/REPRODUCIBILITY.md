# Reproducibility checklist

## Fixed choices reported by the article

- [x] `bert-base-uncased`
- [x] binary classification
- [x] max sequence length = 128
- [x] learning rate = 2e-5
- [x] train batch size = 16
- [x] evaluation batch size = 32
- [x] weight decay = 0.01
- [x] epochs = 3
- [x] cross-entropy loss
- [x] random seed = 42
- [x] standard Dreaddit train/test split
- [x] ECE = 10 equal-width confidence bins
- [x] ACE = 10 equal-frequency confidence bins
- [x] Brier Score uses P(Stress)
- [x] baseline excludes post-hoc calibration and label smoothing

## Details not reported in the paper

The article does not specify an exact frozen set of package versions, GPU model, CUDA
version, OS image, or commit hash. A later reproduction may therefore differ numerically.

Before creating a Zenodo release, run:

```bash
python --version
pip freeze > results/environment_freeze.txt
```

Recommended additional record:

```bash
nvidia-smi > results/nvidia_smi.txt
```

when NVIDIA CUDA is used.

## Comparison template

| Metric | Article | Replication | Absolute difference |
|---|---:|---:|---:|
| Accuracy | 0.7902 |  |  |
| Precision | 0.7800 |  |  |
| Recall | 0.8265 |  |  |
| F1 | 0.8026 |  |  |
| Brier | 0.1565 |  |  |
| ECE | 0.0847 |  |  |
| ACE | 0.0880 |  |  |

Do not manually tune a replication merely to force the reported numbers. If values differ,
report the environment and analyze the cause.
