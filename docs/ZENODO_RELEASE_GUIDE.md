# GitHub → Zenodo release guide

## Recommended repository name

`bert-miscalibration-dreaddit`

## Before the first public release

1. GitHub username already set to `rizaldipiliang` in `CITATION.cff`.
2. Confirm the repository contains **no raw Dreaddit files** and no private credentials.
3. Run the baseline once and add a small results summary if appropriate.
4. Commit `results/environment_freeze.txt`.
5. Check author names and add ORCIDs to `CITATION.cff` / `.zenodo.json` only after verifying them.
6. Push the repository to GitHub.
7. Create a GitHub release, recommended tag: `v1.0.0`.

## Zenodo workflow

1. Sign in to Zenodo.
2. Link your GitHub account.
3. Enable archiving for this repository.
4. Create/publish GitHub release `v1.0.0`.
5. Zenodo will archive that release and mint a DOI.
6. Copy the minted DOI into the repository README.

Suggested badge after DOI exists:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

Replace `XXXXXXX` with the real Zenodo identifier. **Never fabricate a Zenodo DOI.**

## Versioning recommendation

- `v1.0.0`: first verified reproducibility release;
- `v1.0.1`: documentation-only correction;
- `v1.1.0`: added evaluation/error-analysis utility;
- `v2.0.0`: scientifically meaningful extension that changes the experimental package.

Zenodo's concept DOI can point to all versions, while version DOIs identify a specific release.

## Related identifiers

The software archive should be marked as supplementary to:

`10.63158/journalisi.v8i3.1634`

and should reference the Dreaddit paper:

`10.18653/v1/D19-6213`.
