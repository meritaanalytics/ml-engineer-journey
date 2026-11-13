# Machine Learning Engineer Journey: Benson M. Merita

> Mathematician & Data Analyst → Machine Learning Engineer.
> I'm learning in public: every lesson has code, a write-up and a short video.

## Roadmap

Time estimates assume about **10–12 hours a week**. Your maths background shortens the theory, so most of the time goes into code and projects.

| # | Phase | Main topics | Est. time | Portfolio project |
|---|-------|-------------|-----------|-------------------|
| 1 | **Python & tools for ML** | NumPy (vectorised linear algebra), Pandas, Matplotlib/Seaborn, Git & GitHub, Jupyter/VS Code, virtual environments | 3 weeks | *Financial inclusion in East Africa: EDA + baseline* |
| 2 | **Data preparation** | Cleaning, EDA, missing data, outliers, encoding, scaling, feature engineering, data leakage | 3 weeks | *Messy-data cleaning pipeline* (reusable module) |
| 3 | **Core ML concepts** | Supervised vs unsupervised, train/val/test, loss functions, gradient descent, overfitting, bias–variance, cross-validation, metrics | 2 weeks | *Gradient-descent visualiser* (interactive) |
| 4 | **Classic algorithms** | Linear & logistic regression, regularisation, k-NN, naive Bayes, decision trees, random forests, gradient boosting (XGBoost/LightGBM), SVM, k-means, hierarchical clustering, PCA | 7 weeks | *House-price predictor* + *Customer segmentation* |
| 5 | **Evaluation & tuning** | Confusion matrix, precision/recall/F1, ROC/AUC, PR curves, calibration, class imbalance, Grid/Random/Bayesian search, pipelines | 3 weeks | *Credit-risk / loan-default model* (fintech) |
| 6 | **Deep learning** | Neural net from scratch (backprop = chain rule), PyTorch, optimisers, regularisation, CNNs, RNNs, attention & Transformers basics, transfer learning | 7 weeks | *Image classifier* + *Text sentiment model* |
| 7 | **ML engineering** | Clean project structure, testing, FastAPI, Docker, MLflow experiment tracking, data/model versioning, CI/CD basics, cloud deployment, monitoring | 5 weeks | *Deployed churn-prediction API* with Docker |
| 8 | **Capstones & interviews** | 2 end-to-end capstones (e.g. time-series forecaster, recommender), ML system design, coding & theory interview prep, CV and portfolio polish | 5 weeks | *Capstone 1 & 2*, live demos |

**Total: about 35 weeks (8–9 months)** at a steady pace. Faster if you put in more hours, and that's fine too. The goal is depth, not speed.

## Progress tracker

**Current:** 🏁 Phase 1 project: *Who is banked in East Africa?* · *Setup ✅*

### Phase 1: Python & tools for ML
- [x] Environment setup (Miniconda, VS Code, Git)
- [ ] L1 Setup + NumPy: vectors & matrices as the language of ML · *exercises + quiz pending*
- [ ] L2 NumPy II: randomness, `linalg`, PCA from scratch · *exercises + quiz pending*
- [ ] L3 Pandas for ML: groupby as linear algebra, merge, encoding, X/y handoff · *exercises + quiz pending*
- [ ] L4 Visualisation for EDA: fig/ax, KDE from scratch, correlation, Simpson's paradox · *exercises + quiz pending*
- [ ] L5 Git & GitHub: internals (mini-Git) + Git Bash lab, branches, PRs, conflicts · *lab + exercises pending*
- [ ] L6 Reusable Python: the `mlscratch` package, scikit-learn estimator API, pytest, `check_estimator` · *exercises + quiz pending*
- [ ] 🏁 **Phase 1 project:** [Financial inclusion in East Africa](phase1_project_financial_inclusion/PROJECT_BRIEF.md): EDA + baseline model · *in progress*
  - [ ] M1 Data card · [ ] M2 EDA · [ ] M3 Baseline model · [ ] M4 Report & ship

### Phases 2–8
- [ ] Phase 2: Data preparation
- [ ] Phase 3: Core ML concepts
- [ ] Phase 4: Classic algorithms
- [ ] Phase 5: Evaluation & tuning
- [ ] Phase 6: Deep learning
- [ ] Phase 7: ML engineering
- [ ] Phase 8: Capstones & interviews

## Repository layout

```
MachineLearning/
├── README.md                ← this file: roadmap + progress
├── SETUP.md                 ← environment setup (Python, VS Code, Git)
├── requirements.txt
├── .gitignore
├── pyproject.toml           ← makes mlscratch installable: pip install -e .
├── mlscratch/               ← my from-scratch ML package (scikit-learn compatible)
├── tests/                   ← pytest suite: python -m pytest
├── phase1_project_financial_inclusion/   ← 🏁 Phase 1 portfolio project
└── phase1_python_tools/
    ├── lesson01_numpy_for_ml/
    │   ├── lesson01_numpy_for_ml.ipynb   ← the lesson (run it!)
    │   ├── SOCIAL_PACK.md                ← write-up template, video script, captions
    │   └── assets/                       ← charts you generate for posts
    ├── lesson02_random_linalg_pca/
    │   ├── lesson02_random_linalg_pca.ipynb
    │   ├── SOCIAL_PACK.md
    │   └── assets/
    ├── lesson03_pandas_for_ml/
    │   ├── lesson03_pandas_for_ml.ipynb
    │   ├── SOCIAL_PACK.md
    │   └── assets/
    ├── lesson04_visualisation_eda/
    │   ├── lesson04_visualisation_eda.ipynb
    │   ├── SOCIAL_PACK.md
    │   └── assets/
    ├── lesson05_git_github/
    │   ├── lesson05_git_internals.ipynb
    │   ├── GIT_LAB.md                    ← hands-on Git Bash lab
    │   ├── SOCIAL_PACK.md
    │   └── assets/
    └── lesson06_reusable_python/
        ├── lesson06_reusable_python.ipynb
        ├── SOCIAL_PACK.md
        └── assets/
```

## `mlscratch`: my from-scratch ML package

Algorithms from the lessons, written in NumPy and following the scikit-learn estimator API. Every estimator passes scikit-learn's `check_estimator`.

| Class | Lesson | What it does |
|---|---|---|
| `StandardScalerScratch` | L1 | z = (x − μ) / σ via broadcasting |
| `LinearRegressionScratch` | L1, L6 | least squares (`solver="normal"`) or gradient descent with safe step 1/λ_max (`solver="gd"`) |
| `PCAScratch` | L2 | principal components via SVD |

```bash
pip install -e .
python -m pytest        # 12 passed
```

## Connect
- GitHub: [meritaanalytics](https://github.com/meritaanalytics)
- LinkedIn: [benson-merita](https://www.linkedin.com/in/benson-merita/)
