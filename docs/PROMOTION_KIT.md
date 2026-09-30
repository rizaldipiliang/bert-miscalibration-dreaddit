# Academic promotion kit

The goal is **discoverability and legitimate reuse**, not requesting irrelevant citations.

## ResearchGate update

### Short version

A reproducibility package is now available for our 2026 study on confidence miscalibration
in Vanilla BERT-based stress detection using Dreaddit.

The study shows that competitive classification performance does not necessarily imply
reliable confidence estimates. Alongside the baseline classification results, we evaluate
Brier Score, Expected Calibration Error, Adaptive Calibration Error, and confidence-bin
behavior.

Article DOI: https://doi.org/10.63158/journalisi.v8i3.1634

Repository: [ADD GITHUB URL]
Zenodo: [ADD ZENODO DOI AFTER RELEASE]

The code is intended as a diagnostic baseline for research on calibration, uncertainty
estimation, distribution shift, and selective prediction in mental-health NLP.

### Technical version

We have released the reproducibility package accompanying our paper, “An Empirical
Evaluation of Confidence Miscalibration in Vanilla BERT-Based Stress Detection on Social
Media.”

Using the standard Dreaddit split, the Vanilla BERT baseline achieved an F1-score of
0.8026, while calibration analysis produced a Brier Score of 0.1565, ECE of 0.0847, and
ACE of 0.0880. The package provides the baseline training configuration, ECE/ACE
implementation, Brier evaluation, reliability diagram generation, and prediction export.

Article: https://doi.org/10.63158/journalisi.v8i3.1634  
Code: [ADD GITHUB URL]  
Archive: [ADD ZENODO DOI AFTER RELEASE]

We hope the package is useful for reproducibility and for future work on trustworthy NLP.

## LinkedIn post

**New reproducibility resource: confidence calibration in BERT-based stress detection**

I have released a reproducibility package for our 2026 paper:

*An Empirical Evaluation of Confidence Miscalibration in Vanilla BERT-Based Stress
Detection on Social Media.*

The central observation is simple but important: a model can perform well as a classifier
while still producing confidence estimates that are not fully reliable.

Using Vanilla BERT on the Dreaddit benchmark, the study evaluates both predictive
performance and probabilistic reliability through Brier Score, Expected Calibration Error,
Adaptive Calibration Error, and reliability diagrams.

The repository is designed as a baseline for researchers interested in:
- confidence calibration;
- uncertainty estimation;
- mental-health NLP;
- distribution shift; and
- selective prediction.

Article DOI: https://doi.org/10.63158/journalisi.v8i3.1634  
GitHub: [ADD GITHUB URL]  
Zenodo: [ADD ZENODO DOI AFTER RELEASE]

Feedback, replication results, and scientifically relevant extensions are welcome.

#NLP #BERT #MachineLearning #TrustworthyAI #Calibration #MentalHealthNLP #ReproducibleResearch

## Outreach email / direct message — concise

Subject: Reproducible Vanilla BERT calibration baseline on Dreaddit

Dear Dr. [Surname],

I recently read your work on [SPECIFIC TOPIC/PAPER] and thought our reproducibility
resource might be relevant to your research.

We evaluated Vanilla BERT on Dreaddit not only for classification performance but also
for confidence reliability using Brier Score, ECE, ACE, and reliability-bin analysis. The
code and evaluation pipeline are available here:

Article: https://doi.org/10.63158/journalisi.v8i3.1634  
Repository: [ADD GITHUB URL]

I am sharing it in case the baseline or calibration implementation is useful for your own
experiments. No action is expected; I would also be interested in any replication feedback.

Best regards,  
Rizaldi

## Outreach email — calibration/uncertainty researcher

Subject: Dreaddit baseline for calibration and uncertainty research

Dear Dr. [Surname],

Your work on [CALIBRATION / UNCERTAINTY / SELECTIVE PREDICTION TOPIC] is closely
related to a baseline we recently released for social-media stress detection.

The study evaluates `bert-base-uncased` on the standard Dreaddit split and explicitly
separates discriminative performance from probabilistic reliability. In addition to
accuracy/F1, we report Brier Score, ECE, ACE, confidence-bin behavior, and
high-confidence error patterns.

Paper: https://doi.org/10.63158/journalisi.v8i3.1634  
Reproducibility package: [ADD GITHUB URL]  
Zenodo archive: [ADD AFTER RELEASE]

I am sharing it because the baseline may provide a useful reference point for future work
on post-hoc calibration, uncertainty estimation, distribution shift, or selective prediction.
If you happen to reproduce or extend it, I would be very interested in the resulting
observations.

Kind regards,  
Rizaldi

## Outreach rules

Do:
- contact only researchers whose work is genuinely related;
- mention one concrete connection to their paper;
- share a usable resource;
- invite replication or technical feedback.

Do not:
- ask for a citation;
- offer reciprocal citation;
- mass-message unrelated researchers;
- imply that citation is expected;
- send the same generic message to hundreds of authors.
