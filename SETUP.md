# Setup Guide (Windows)

You'll do this once. It takes about 45 minutes. Every later lesson assumes it's done.

## 1. Install the tools

| Tool | Why | Get it |
|------|-----|--------|
| **Miniconda** (Python 3.12) | Manages Python versions and isolated environments | anaconda.com/download → *Miniconda* installer |
| **VS Code** | Your main editor: notebooks, scripts, Git, terminal | code.visualstudio.com |
| **Git for Windows** | Includes **Git Bash**, which you'll use for every GitHub upload | git-scm.com |
| **Google Colab** (browser) | Free GPU for the deep-learning phase | colab.research.google.com |

**VS Code extensions** (Ctrl+Shift+X): *Python*, *Jupyter*, *Pylance*, *GitLens* (optional), *Rainbow CSV* (optional).

> If you already have Python installed some other way, that's fine. Section 2 has a `venv` alternative.

## 2. Create an ML environment

**Why:** each project gets its own isolated set of package versions, so upgrading one project never breaks another. Production ML teams work the same way.

Open **Anaconda Prompt** (or Git Bash once conda is initialised) and run:

```bash
cd "/c/Users/ole merit/Desktop/DATASCIENCE/MAdatascience/MachineLearning"
conda create -n ml python=3.12 -y
conda activate ml
pip install -r requirements.txt
python -m ipykernel install --user --name ml --display-name "Python (ml)"
```

*Alternative without conda (plain Python 3.11+):*
```bash
python -m venv .venv
source .venv/Scripts/activate      # Git Bash on Windows
pip install -r requirements.txt
```

**Check it worked:**
```bash
python -c "import numpy, pandas, sklearn, matplotlib; print('numpy', numpy.__version__, '| sklearn', sklearn.__version__)"
```

## 3. Open the lesson in VS Code

1. In VS Code: *File → Open Folder…* → `MachineLearning`.
2. Open `phase1_python_tools/lesson01_numpy_for_ml/lesson01_numpy_for_ml.ipynb`.
3. Top right: *Select Kernel* → **Python (ml)**.
4. Click *Run All*. Every cell should run without errors.

## 4. Git + GitHub (Git Bash)

One-time identity setup:
```bash
git config --global user.name "Benson M. Merita"
git config --global user.email "your-github-email@example.com"
git config --global init.defaultBranch main
```

Turn this folder into a repo and push it:
```bash
cd "/c/Users/ole merit/Desktop/DATASCIENCE/MAdatascience/MachineLearning"
git init
git add .
git commit -m "Start ML engineer journey: roadmap + lesson 1"
```
Then on github.com create an **empty** repo called `ml-engineer-journey` (no README, no .gitignore) and run:
```bash
git remote add origin https://github.com/meritaanalytics/ml-engineer-journey.git
git push -u origin main
```

After each lesson:
```bash
git add .
git commit -m "Lesson 1: NumPy for ML (vectorised predictions, MSE, gradient)"
git push
```

> **Commit habit:** use small commits with messages that say *what changed and why*. Recruiters do read commit histories.
