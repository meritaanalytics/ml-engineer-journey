# Who Is Banked in East Africa? Financial Inclusion EDA & Baseline Model

*Phase 1 project · ML Engineer Journey · Benson M. Merita*

> **TL;DR:** _[1–2 sentences: the single most important finding + how well the baseline model does vs the naive baseline.]_

## 1. Problem
_[Why financial inclusion matters in East Africa; who would use this analysis (a bank, a fintech, a regulator); the two goals: explain and predict.]_

## 2. Data
- **Source:** Zindi, *Financial Inclusion in Africa* (FinScope surveys, 2016–2018). See [`data/README.md`](data/README.md) to reproduce.
- **Size:** _[rows]_ respondents · _[n]_ features · countries: Kenya, Rwanda, Tanzania, Uganda
- **Target:** `bank_account`: _[x]_% have an account
- **Limitations:** _[survey years differ by country? self-reported? anything else you found]_

## 3. Key findings
1. _[Finding + number + chart reference]_
2. _
3. _
4. _
5. _

![_[main chart]_](figures/_[file]_.png)

## 4. Model
**Approach:** _[pipeline: encoding choices, scaler from my `mlscratch` package, linear probability model, threshold 0.5]_

| Model | CV accuracy (mean ± std) | Test accuracy | Test MAE |
|---|---|---|---|
| Majority class ("no account") | | | |
| One-feature baseline: _[feature]_ | | | |
| **Linear probability model (all features)** | | | |

**Confusion matrix (test):** _[image or table + one sentence about which errors dominate]_

**Most influential coefficients:** _[top 5, interpreted as differences from the baseline category]_

## 5. Limitations & next steps
- _[e.g. linear probability model can predict < 0 or > 1 → Phase 4: logistic regression]_
- _[accuracy with ~14% positives → Phase 5: precision/recall, ROC-AUC]_
- _[associations, not causes]_

## 6. Reproduce
```bash
pip install -e ../            # installs mlscratch from the repo root
# put Train.csv in data/raw/ (see data/README.md), then run notebooks 01 -> 03
```

## Repository
`notebooks/01_data_card.ipynb` · `notebooks/02_eda.ipynb` · `notebooks/03_baseline_model.ipynb` · `src/fi_utils.py`
