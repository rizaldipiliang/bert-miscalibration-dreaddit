# Dataset note: Dreaddit

## Provenance

Dreaddit was introduced by **Elsbeth Turcan and Kathy McKeown (2019)** for stress
analysis in social media. The original work describes a multi-domain Reddit corpus and
approximately 3.5K human-labeled segments.

**Canonical citation:**  
Turcan, E., & McKeown, K. (2019). *Dreaddit: A Reddit Dataset for Stress Analysis in
Social Media.* Proceedings of the Tenth International Workshop on Health Text Mining and
Information Analysis, 97–107. DOI: 10.18653/v1/D19-6213.

## Split used in the 2026 article

- training: 2,838 segments;
- test: 715 segments;
- total: 3,553 segments;
- positive class: `Stress`;
- negative class: `Not Stress`.

## Important ethical interpretation

The labels should be treated as **text-based stress indications**, not clinical diagnoses.
Do not use this baseline for diagnosis or individual-level health decisions.

## Distribution

This repository does not redistribute raw Reddit-derived text. Obtain the data from the
original source or another source whose terms you have verified. Keep the raw data out of
Git history; `.gitignore` is already configured for this.
