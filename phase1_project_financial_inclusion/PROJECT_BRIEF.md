# 🏁 Phase 1 Portfolio Project: Who Is Banked in East Africa?

**Type:** end-to-end EDA + baseline model · **Effort:** about 10–14 hours over 1–2 weeks · **Mode:** *you* write all the code; I review.

---

## 1. Problem statement

Across Kenya, Rwanda, Tanzania and Uganda, only a minority of adults have a formal bank account, even as mobile money spreads. Banks, fintechs and policymakers want to know **who is excluded, and why**, to design products and outreach.

**Your job:**
1. **Explain:** use EDA to find which demographic and economic factors are associated with having a bank account, and how this differs between countries.
2. **Predict:** build a reproducible baseline model that estimates the probability a person has a bank account, and evaluate it honestly.

This is what a junior data scientist at a Kenyan bank or fintech might do in their first month. Phase 4 (logistic regression, trees) and Phase 5 (metrics, imbalance) will come back to this same dataset to improve the model, so you'll have a visible "v1 → v2 → v3" story on GitHub.

---

## 2. Dataset

**Financial Inclusion in Africa** (Zindi, with the Financial Sector Deepening network). Respondents are drawn from FinScope household surveys, 2016–2018.

| | |
|---|---|
| Where | <https://zindi.africa/competitions/financial-inclusion-in-africa/data> (free Zindi account; join the competition to download) |
| Files you need | `Train.csv` (has the target), `VariableDefinitions.csv` |
| Rows (train) | about 23,500 respondents |
| Target | `bank_account` (Yes/No) |
| Features | country, year, location type (rural/urban), cellphone access, household size, age, gender, relationship with household head, marital status, education level, job type |

⚠️ **Data terms:** Zindi's data belongs to Zindi and the host. **Do not commit the CSVs to GitHub.** Put them in `data/raw/` (git-ignored) and explain in `data/README.md` how to download them. That's also the professional habit for any dataset.

---

## 3. Milestones

Work on a branch: `git switch -c phase1-project`. Commit after each milestone, and open **one pull request** at the end (or one per milestone if you want feedback sooner).

### M1 · Data card (≈ 2 h) → `notebooks/01_data_card.ipynb`
- [ ] Download the data into `data/raw/`; fill in `data/README.md` (source, date downloaded, licence note)
- [ ] Shape, dtypes, missing values, duplicates, unique values per column (reuse your Lesson 3 `profile()` function from Exercise 1)
- [ ] Target balance: % with an account, overall and **per country**
- [ ] Check every column: what does it mean, what type is it (numeric / nominal / ordinal), and could it leak the target?
- [ ] Write a short **data card**: what one row represents, where the data came from, known limitations (survey years differ by country, self-reported, etc.)

### M2 · Exploratory analysis (≈ 4 h) → `notebooks/02_eda.ipynb`
Answer at least these **questions**, each with one clear chart and 1–3 sentences of interpretation:
- [ ] Q1. How does account ownership vary by **country**? By **year**? (Are country and year confounded?)
- [ ] Q2. By **education level**: is there a gradient?
- [ ] Q3. By **job type**: which groups are most and least banked? Report the **counts** too (small groups mislead).
- [ ] Q4. By **location type** and **cellphone access**.
- [ ] Q5. By **age**: use a histogram/KDE split by the target (Lesson 4). Is the relationship linear?
- [ ] Q6. **Gender:** what is the raw gap, and does it persist *within* education levels and job types? (Lesson 4's Simpson check.)
- [ ] Q7. **Country gap revisited:** do country differences shrink once you condition on education and location? Use a pivot table/heatmap.
- [ ] Q8. One question of **your own**, which should be the most interesting one.
- [ ] End with a **"Top 5 findings"** cell written for a non-technical bank manager.

### M3 · Baseline model (≈ 4 h) → `notebooks/03_baseline_model.ipynb`
- [ ] Hold out a **stratified test set** (20%) *before* any modelling decisions; set `random_state` everywhere (Lesson 2)
- [ ] Build a `Pipeline` + `ColumnTransformer`: one-hot (`drop="first"`) for nominal features, `StandardScalerScratch` from **your `mlscratch`** for numeric features, and an encoding choice you justify for `education_level` (ordinal or one-hot?)
- [ ] Model: `LinearRegressionScratch` on the 0/1 target. That's a **linear probability model**: predictions estimate P(account). Threshold at 0.5 to classify.
- [ ] **Baselines first:** (a) the majority class ("nobody has an account"), (b) a one-feature model of your choice. Your model must be compared against both.
- [ ] Report on the test set: **accuracy**, the **confusion matrix** (`sklearn.metrics.confusion_matrix`), and **MAE** of the predicted probabilities, plus 5-fold CV accuracy on the training set (mean ± std)
- [ ] Interpret the 10 largest coefficients: what does each mean *as a difference from the baseline category* (Lesson 3)?
- [ ] Honest limitations: what's wrong with a linear probability model? (Hint: look at the range of your predictions.) Phase 4 fixes this with logistic regression.
- [ ] *Stretch:* submit predictions on `Test.csv` to the Zindi leaderboard and record your score (check the competition's *Evaluation* tab for the metric).

### M4 · Report & ship (≈ 2 h)
- [ ] Fill in this folder's `README.md`: problem, data, approach, key charts (saved to `figures/`), results table, findings, limitations, next steps
- [ ] Every notebook runs top to bottom from a fresh kernel (*Restart & Run All*)
- [ ] Pull request merged into `main`, then pushed; add the project to your top-level README
- [ ] Post it (see `SOCIAL_PACK.md`)

---

## 4. What "good" looks like (rubric)

| Area | Needs work | Good | Excellent |
|---|---|---|---|
| **Reproducibility** | Hard-coded paths, cells out of order | Runs top-to-bottom; seeds set; data instructions in `data/README.md` | Also: helper functions in `src/`, a pinned environment, a one-line way to re-run |
| **Data understanding** | Jumps straight to plots | Data card with types, balance, limitations | Spots confounding (country × year), questions survey design |
| **EDA** | Many default charts, no interpretation | Each question → one labelled chart + a sentence | Group-aware (Simpson checks), counts shown, findings ranked by importance |
| **Modelling** | No baseline, or test set used for decisions | Pipeline, held-out test, majority baseline, CV | Explains *why* accuracy alone misleads at ~14% positives; error analysis of the confusion matrix |
| **Rigour & honesty** | Correlation stated as causation | Associations described as associations | Explicit limitations section; says what *can't* be concluded |
| **Code quality** | Copy-pasted cells, magic numbers | Functions, clear names, comments | Reuses `mlscratch`; small tests for any helper you write |
| **Communication** | Notebook dump | README report with figures and a results table | A bank manager could read the "Top 5 findings" and act on them |

---

## 5. Repository layout (already scaffolded)

```
phase1_project_financial_inclusion/
├── PROJECT_BRIEF.md          ← this file
├── README.md                 ← your report (template provided; fill it in)
├── SOCIAL_PACK.md            ← post/video templates for the finished project
├── data/
│   ├── README.md             ← how to get the data (fill in)
│   └── raw/                  ← Train.csv etc. go here (git-ignored)
├── notebooks/
│   ├── 01_data_card.ipynb    ← skeleton: headings + TODOs
│   ├── 02_eda.ipynb
│   └── 03_baseline_model.ipynb
├── src/
│   └── fi_utils.py           ← helper stubs for you to implement
└── figures/                  ← save charts here for the README
```

---

## 6. How I'll review

When you open the pull request, send me the link (or the notebooks). I'll review it the way a senior data scientist would: what's solid, what's wrong, and what to change, with hints before answers. Expect honest feedback against the rubric above.

**Rules of the game:** look things up in the docs and your own Lesson notebooks freely. If you're stuck for more than 30 minutes, ask me for a *hint* (not the answer), and say which milestone and what you tried.
