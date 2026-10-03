# Project Roadmap

## Project Status

The repository currently contains a working baseline credit-risk analytics pipeline covering:

- Dataset loading and validation
- Descriptive statistics and default-rate analysis
- Correlation analysis
- Missing-value and distribution visualizations
- Preprocessing for numerical and categorical variables
- Logistic-regression baseline model
- Stratified train/test evaluation
- Accuracy, precision, recall, F1, and ROC-AUC
- Classification report
- Basic dataset test coverage

The roadmap below reflects the current implementation rather than the original project plan.

---

## Phase 1 — Data & Exploratory Analysis

- [x] Repository structure and documentation
- [x] Import credit-risk dataset
- [x] Dataset inspection and summary statistics
- [x] Missing-value analysis
- [x] Default-rate analysis
- [x] Loan/credit descriptive statistics
- [x] Correlation analysis
- [x] Distribution visualizations
- [ ] Document dataset provenance
- [ ] Document target-variable definition
- [ ] Document the economic meaning of the available variables
- [ ] Document known dataset limitations
- [ ] Add explicit data-quality validation checks
- [ ] Check class balance and document its implications for model evaluation

---

## Phase 2 — Baseline Credit-Risk Model

- [x] Define target variable
- [x] Separate features and target
- [x] Identify numerical and categorical variables
- [x] Standardize numerical features
- [x] One-hot encode categorical features
- [x] Build reproducible preprocessing/model pipeline
- [x] Train logistic-regression baseline
- [x] Use stratified train/test split
- [x] Evaluate accuracy
- [x] Evaluate precision
- [x] Evaluate recall
- [x] Evaluate F1 score
- [x] Evaluate ROC-AUC
- [x] Generate classification report
- [x] Generate confusion matrix information
- [ ] Add ROC curve
- [ ] Add precision-recall curve
- [ ] Add cross-validation
- [ ] Report fold-level performance variability
- [ ] Add confidence intervals where statistically appropriate

---

## Phase 3 — Probability of Default & Model Validation

The model's predicted probabilities should be treated as candidate Probability of Default (PD) estimates only after appropriate validation.

- [ ] Evaluate predicted-probability calibration
- [ ] Add calibration curve
- [ ] Add Brier score
- [ ] Compare predicted and observed default frequencies
- [ ] Evaluate ROC-AUC alongside PR-AUC
- [ ] Analyse performance under class imbalance
- [ ] Evaluate threshold-dependent performance
- [ ] Document the trade-off between false positives and false negatives
- [ ] Analyse sensitivity and specificity across thresholds
- [ ] Identify an appropriate decision threshold only if justified by the project's objective
- [ ] Document the distinction between classification performance and probability quality
- [ ] Compare model performance across validation folds
- [ ] Assess whether the model is sufficiently stable for interpretation

---

## Phase 4 — Model Comparison

The objective is to determine whether additional model complexity provides meaningful improvement over the logistic-regression benchmark.

- [x] Establish logistic regression as the baseline model
- [ ] Add one nonlinear benchmark model
- [ ] Compare models using the same train/test and cross-validation framework
- [ ] Compare ROC-AUC
- [ ] Compare PR-AUC
- [ ] Compare F1 score
- [ ] Compare recall and precision
- [ ] Compare probability calibration
- [ ] Compare computational complexity
- [ ] Compare interpretability
- [ ] Document model-selection criteria
- [ ] Avoid model-comparison claims unless models are evaluated under equivalent conditions
- [ ] Avoid adding additional models without analytical justification

Potential benchmark models:

- Random Forest
- Gradient Boosting
- HistGradientBoosting
- XGBoost, if justified by project scope

The purpose of additional models is benchmarking rather than maximizing the number of algorithms.

---

## Phase 5 — Model Explainability & Risk Interpretation

- [ ] Analyse logistic-regression coefficients after preprocessing
- [ ] Convert relevant coefficients into interpretable effects where appropriate
- [ ] Identify statistically and economically meaningful risk indicators
- [ ] Analyse feature contributions for nonlinear models
- [ ] Add permutation importance where appropriate
- [ ] Consider SHAP-based analysis for nonlinear models
- [ ] Compare explainability across model classes
- [ ] Distinguish predictive association from causal effects
- [ ] Document limitations of feature-importance methods
- [ ] Avoid interpreting model importance as evidence of causality
- [ ] Document potential data and measurement biases

---

## Phase 6 — Credit Portfolio Analytics

Move from individual borrower predictions toward aggregate credit-risk analysis where the dataset permits.

- [ ] Aggregate borrower-level predictions into portfolio-level measures
- [ ] Analyse observed default rates across borrower segments
- [ ] Analyse predicted risk across borrower segments
- [ ] Examine risk concentration
- [ ] Identify high-risk borrower segments
- [ ] Compare observed and predicted default rates by segment
- [ ] Analyse portfolio-level distribution of predicted PD
- [ ] Introduce expected-loss concepts where the required inputs are available
- [ ] Clearly distinguish Probability of Default (PD)
- [ ] Clearly distinguish Loss Given Default (LGD)
- [ ] Clearly distinguish Exposure at Default (EAD)
- [ ] Estimate Expected Loss only when the necessary assumptions and inputs are available
- [ ] Add scenario or sensitivity analysis where supported by the data
- [ ] Clearly state which risk quantities are observed, estimated, or assumed

---

## Phase 7 — Results & Research Reporting

The project should contain actual empirical findings rather than only descriptions of implemented methods.

- [ ] Create a reproducible results table
- [ ] Report dataset characteristics
- [ ] Report class distribution
- [ ] Report baseline model performance
- [ ] Report cross-validation results
- [ ] Report probability-calibration results
- [ ] Report threshold analysis
- [ ] Report model-comparison results
- [ ] Report important risk indicators
- [ ] Report segment-level findings
- [ ] Add publication-style figures
- [ ] Add ROC curves
- [ ] Add precision-recall curves
- [ ] Add calibration plots
- [ ] Add confusion matrices
- [ ] Add feature-importance or coefficient plots
- [ ] Add portfolio/segment risk visualizations where appropriate
- [ ] Update `RESULTS.md` with actual generated results
- [ ] Add a concise interpretation of the main findings
- [ ] Document model limitations
- [ ] Document data limitations
- [ ] Document external-validity limitations
- [ ] Ensure every reported numerical result can be reproduced from the repository

---

## Phase 8 — Statistical & Risk Validation

- [ ] Check model performance across multiple validation folds
- [ ] Evaluate performance stability
- [ ] Examine class imbalance effects
- [ ] Evaluate calibration stability
- [ ] Examine potential overfitting
- [ ] Check whether preprocessing is performed within the validation pipeline
- [ ] Ensure no information from the test set enters model training
- [ ] Document the train/test methodology
- [ ] Document random seeds and reproducibility settings
- [ ] Analyse model limitations under distribution shift where possible
- [ ] Document the difference between in-sample, validation, and out-of-sample evidence

---

## Phase 9 — Engineering & Reproducibility

- [ ] Expand automated tests beyond dataset loading
- [ ] Add preprocessing tests
- [ ] Add model-output tests
- [ ] Add metric-calculation tests
- [ ] Add tests for edge cases
- [ ] Add tests for missing or unexpected columns
- [ ] Add tests for invalid target values
- [ ] Add tests for empty or malformed datasets
- [ ] Pin or constrain dependency versions where appropriate
- [ ] Add a reproducible execution command
- [ ] Add continuous integration
- [ ] Run automated tests on every repository update
- [ ] Keep documentation synchronized with the implemented code
- [ ] Ensure generated figures and results can be recreated from source code

---

## Phase 10 — Documentation Quality

- [ ] Update `README.md` to reflect the current implementation
- [ ] Update `PROJECT.md`
- [ ] Update `RESULTS.md`
- [ ] Keep `ROADMAP.md` synchronized with completed work
- [ ] Remove obsolete development plans
- [ ] Document dataset provenance
- [ ] Document assumptions
- [ ] Document modelling methodology
- [ ] Document evaluation methodology
- [ ] Document limitations
- [ ] Document reproducibility instructions
- [ ] Document the distinction between analytical demonstration and production credit-risk modelling

---

## Optional Extension — Interactive Dashboard

The dashboard is intentionally secondary to the analytical and modelling pipeline.

A dashboard should present validated analytical results rather than substitute for model validation.

- [ ] Define dashboard requirements
- [ ] Add interactive borrower-risk views
- [ ] Add portfolio-level risk views
- [ ] Display default-rate analysis
- [ ] Display model performance
- [ ] Display calibration diagnostics
- [ ] Display segment-level risk analysis
- [ ] Display model explanations
- [ ] Add filtering by relevant borrower characteristics
- [ ] Clearly distinguish observed data from model predictions
- [ ] Document the dashboard as a presentation layer

---

# Definition of Done

The project should be considered complete when:

1. The dataset and its provenance are clearly documented.
2. The target variable is explicitly defined.
3. Data-quality checks are implemented.
4. The exploratory analysis is reproducible.
5. The logistic-regression baseline is fully documented.
6. The validation methodology is appropriate for the dataset and target.
7. Performance is reported using metrics appropriate to the class distribution.
8. Predicted probabilities are evaluated for calibration before being interpreted as Probability of Default.
9. Threshold-dependent performance is documented where relevant.
10. At least one additional model is evaluated only if it adds meaningful analytical value.
11. Model comparison uses a consistent validation framework.
12. Risk indicators are interpreted without unsupported causal claims.
13. Portfolio-level analysis is included where the available data permit it.
14. Results are generated directly from repository code.
15. `RESULTS.md` contains actual empirical findings rather than only a description of functionality.
16. Figures and tables are reproducible.
17. Automated tests cover the core analytical pipeline.
18. Dependencies and execution instructions are documented.
19. `README.md`, `PROJECT.md`, `RESULTS.md`, and `ROADMAP.md` accurately describe the current state of the project.
20. The project clearly distinguishes a research/analytics prototype from a production lending-decision system.

---

# Scope Discipline

This project is designed as a **credit-risk analytics study and modelling prototype**, not as a production lending-decision system.

The roadmap therefore prioritizes:

**data quality → validation → probability calibration → model interpretation → portfolio analysis → empirical results → reproducibility**

over adding increasingly complex models or interfaces without corresponding analytical justification.

Additional models, dashboards, and techniques should only be introduced when they answer a specific analytical question or materially improve validation, interpretation, or reproducibility.

The primary objective is a rigorous and reproducible credit-risk analysis rather than the maximum number of machine-learning algorithms.
