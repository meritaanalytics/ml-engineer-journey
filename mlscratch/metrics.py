"""Evaluation metrics written from scratch."""
import numpy as np


def mean_squared_error(y_true, y_pred) -> float:
    """MSE = (1/n) * ||y_pred - y_true||^2."""
    y_true, y_pred = np.asarray(y_true, dtype=float), np.asarray(y_pred, dtype=float)
    if y_true.shape != y_pred.shape:
        raise ValueError(f"shape mismatch: y_true {y_true.shape} vs y_pred {y_pred.shape}")
    r = y_pred - y_true
    return float(r @ r / r.size)
