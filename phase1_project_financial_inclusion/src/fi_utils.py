"""Helper functions for the Financial Inclusion project.

These are STUBS: implement them yourself (that's part of the project).
Import them in the notebooks with:

    import sys; sys.path.insert(0, "../src")
    from fi_utils import load_train, profile, rate_by

Tip: once a function works, add a tiny test for it (see tests/ at the repo root).
"""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def load_train(path: Path | str = DATA_DIR / "Train.csv") -> pd.DataFrame:
    """Load Train.csv and return a DataFrame with:
    - a 0/1 integer target column `bank_account` (from "Yes"/"No")
    - categorical columns as pandas 'category' dtype
    - `education_level` as an ORDERED categorical (decide and document the order)

    Raises FileNotFoundError with a helpful message (pointing to data/README.md) if the file is missing.
    """
    raise NotImplementedError("TODO: implement load_train")


def profile(df: pd.DataFrame) -> pd.DataFrame:
    """One row per column: dtype, % missing, n unique, an example value. (Lesson 3, Exercise 1.)"""
    raise NotImplementedError("TODO: implement profile")


def rate_by(df: pd.DataFrame, by: str | list[str], target: str = "bank_account") -> pd.DataFrame:
    """Account-ownership rate AND count per group, sorted by rate (descending).

    Always return the count next to the rate: small groups produce misleading rates.
    """
    raise NotImplementedError("TODO: implement rate_by")


def save_fig(fig, name: str) -> Path:
    """Save a Matplotlib figure to ../figures/<name>.png at dpi=150 with a tight bbox; return the path."""
    raise NotImplementedError("TODO: implement save_fig")
