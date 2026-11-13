# Lesson 5 · Git Lab (Git Bash, your real repository)

Do this in **Git Bash** (Start menu → "Git Bash"). Every command here is safe: nothing deletes your files.
Time: about 60–90 minutes the first time.

> **Notation:** lines starting with `$` are commands (type them without the `$`). Lines starting with `#` are comments.

---

## Part 0 · One-time configuration

```bash
$ git --version                                   # any 2.4x+ is fine
$ git config --global user.name  "Benson M. Merita"
$ git config --global user.email "YOUR-GITHUB-EMAIL"     # must match your GitHub account to link commits to your profile
$ git config --global init.defaultBranch main
$ git config --global core.autocrlf true          # Windows: convert line endings sensibly
$ git config --global core.editor "code --wait"   # commit messages open in VS Code
$ git config --global --list                      # check everything
```

> 💡 To keep your email private, use GitHub's no-reply address: GitHub → Settings → Emails → "Keep my email address private". Copy the `…@users.noreply.github.com` address and use it above.

---

## Part 1 · Turn the folder into a repository, with a meaningful history

```bash
$ cd "/c/Users/ole merit/Desktop/DATASCIENCE/MAdatascience/MachineLearning"
$ git init
$ git status                       # everything is "untracked"
```

Instead of one giant commit, build a history that tells your story, one commit per logical piece:

```bash
$ git add README.md SETUP.md requirements.txt .gitignore
$ git commit -m "Set up ML engineer journey: roadmap, setup guide, requirements"

$ git add phase1_python_tools/lesson01_numpy_for_ml
$ git commit -m "Lesson 1: NumPy for ML: vectorised predict, MSE, gradient (+ sklearn check)"

$ git add phase1_python_tools/lesson02_random_linalg_pca
$ git commit -m "Lesson 2: randomness, linalg and PCA from scratch (matches sklearn)"

$ git add phase1_python_tools/lesson03_pandas_for_ml
$ git commit -m "Lesson 3: Pandas for ML: groupby as least squares, dummy trap, X/y handoff"

$ git add phase1_python_tools/lesson04_visualisation_eda
$ git commit -m "Lesson 4: EDA visualisation: KDE from scratch, Simpson's paradox"

$ git add phase1_python_tools/lesson05_git_github
$ git commit -m "Lesson 5: Git internals: mini-Git with real Git object IDs"

$ git log --oneline --graph        # your history so far
$ git status                       # "nothing to commit, working tree clean"
```

**Commit message habit:** imperative mood, under ~72 characters, saying *what changed* (and *why* if it isn't obvious).

---

## Part 2 · Put it on GitHub

1. Go to **github.com → + → New repository**.
   - Name: `ml-engineer-journey`
   - Description: *Mathematician → ML Engineer: learning ML from first principles, in public.*
   - **Public**. Do **not** add a README, .gitignore or licence (you already have them).
2. Back in Git Bash:

```bash
$ git remote add origin https://github.com/meritaanalytics/ml-engineer-journey.git
$ git remote -v                    # check the URL
$ git push -u origin main
```

The first push opens a **browser sign-in** (Git Credential Manager, bundled with Git for Windows). Approve it once and it's remembered.

3. Refresh the GitHub page. Your README renders with the roadmap, and notebooks render with their outputs and charts.

---

## Part 3 · Make the repository recruiter-ready (5 minutes)

- On the repo page, click ⚙️ next to **About**: add the description, **topics** (`machine-learning`, `python`, `numpy`, `data-science`, `learning-in-public`), and your LinkedIn as the website.
- **Pin it:** your GitHub profile → *Customize your pins* → select `ml-engineer-journey`.
- Optional but strong: create a **profile README** (a repo named exactly `meritaanalytics`) introducing yourself as *Mathematician & Data Analyst → ML Engineer*.

---

## Part 4 · The everyday workflow: branch → commit → push → pull request → merge

This is how teams work, and how you'll submit exercises to me from now on.

```bash
# 1. start from an up-to-date main
$ git switch main
$ git pull

# 2. create a branch for one piece of work
$ git switch -c exercises

# 3. do the work: put your exercise notebooks in each lesson folder, e.g.
#    phase1_python_tools/lesson01_numpy_for_ml/lesson01_exercises.ipynb
$ git status
$ git add phase1_python_tools/*/lesson0*_exercises.ipynb
$ git commit -m "Add exercises for lessons 1-4"

# 4. publish the branch
$ git push -u origin exercises
```

5. GitHub shows a yellow banner: **Compare & pull request**. Click it.
   - Title: *Exercises: lessons 1–4*
   - Description: what you did, what you found hard, any questions.
   - **Create pull request**, then review the **Files changed** tab (that's the LCS diff from the notebook), then **Merge pull request**.

```bash
# 6. bring the merged work home and tidy up
$ git switch main
$ git pull
$ git branch -d exercises                 # delete the local branch (its commits are safe in main)
$ git log --oneline --graph --all
```

---

## Part 5 · Conflict drill (do it once on purpose, then you won't fear it)

```bash
$ git switch -c drill
# edit README.md: change the line "**Current:** ..." to  **Current:** drill branch
$ git commit -am "Drill: change current status on branch"

$ git switch main
# edit the SAME line in README.md to:  **Current:** main branch
$ git commit -am "Drill: change current status on main"

$ git merge drill                          # CONFLICT (content): Merge conflict in README.md
$ git status                               # shows "both modified: README.md"
```

Open `README.md` in VS Code. You'll see:

```
<<<<<<< HEAD
**Current:** main branch
=======
**Current:** drill branch
>>>>>>> drill
```

VS Code offers *Accept Current / Incoming / Both*. Choose, or edit by hand, so that only the line you want remains (with **no markers**). Then:

```bash
$ git add README.md
$ git commit -m "Resolve drill conflict"
$ git branch -d drill
$ git push
```

---

## Cheat sheet

| I want to… | Command |
|---|---|
| See what changed | `git status`, `git diff`, `git diff --staged` |
| Stage / unstage | `git add <file>` / `git restore --staged <file>` |
| Throw away *uncommitted* edits to a file ⚠️ | `git restore <file>` |
| Fix the last commit message (not pushed yet) | `git commit --amend` |
| Undo a **pushed** commit safely | `git revert <hash>` (makes a new "undo" commit) |
| See history | `git log --oneline --graph --all` |
| Who changed this line? | `git blame <file>` |
| Park unfinished work | `git stash` / `git stash pop` |
| Get teammates' changes | `git pull` |

**Never** `git push --force` to `main`. **Never** commit API keys or passwords. If it happens, rotate the key immediately: deleting it in a new commit doesn't remove it from history.

**File-size limits:** GitHub rejects files over 100 MB and warns above 50 MB. Keep raw datasets out of Git (`data/raw/` is already in your `.gitignore`), and link to their source in the README instead.
