# Dreaddit data placement

The raw Dreaddit dataset is intentionally **not bundled** in this repository.

Original dataset paper:

- Elsbeth Turcan and Kathy McKeown (2019), *Dreaddit: A Reddit Dataset for Stress Analysis in Social Media*
- ACL Anthology: https://aclanthology.org/D19-6213/
- DOI: https://doi.org/10.18653/v1/D19-6213

A public data location has also been referenced by subsequent research:
`http://www.cs.columbia.edu/~eturcan/data/dreaddit.zip`

Before redistributing any copy, verify the current terms from the original source.

Expected local layout:

```text
data/raw/
├── dreaddit-train.csv
└── dreaddit-test.csv
```

The 2026 article reports 2,838 training segments and 715 test segments (3,553 total).
Some mirrored copies may differ by one row or in column naming. Preserve the source
version you actually use and document any discrepancy rather than silently editing data.
