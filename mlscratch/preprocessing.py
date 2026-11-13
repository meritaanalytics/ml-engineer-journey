"""Feature scaling from scratch (Lesson 1: broadcasting)."""
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted, validate_data


class StandardScalerScratch(TransformerMixin, BaseEstimator):
    """Standardise features: z = (x - mean) / std, column by column.

    Parameters
    ----------
    with_mean : bool, default=True
        Subtract the column mean.
    with_std : bool, default=True
        Divide by the column standard deviation (population std, ddof=0, like scikit-learn).

    Attributes
    ----------
    (learned in ``fit``; a trailing underscore means "learned from data")
    mean_ : ndarray of shape (n_features,)
    scale_ : ndarray of shape (n_features,)
    n_features_in_ : int
    """

    def __init__(self, with_mean=True, with_std=True):
        # API rule: __init__ only STORES the hyperparameters, unchanged. No validation, no computation.
        self.with_mean = with_mean
        self.with_std = with_std

    def fit(self, X, y=None):
        X = validate_data(self, X, dtype=float)            # checks X, records n_features_in_
        self.mean_ = X.mean(axis=0) if self.with_mean else np.zeros(X.shape[1])
        std = X.std(axis=0) if self.with_std else np.ones(X.shape[1])
        self.scale_ = np.where(std == 0, 1.0, std)         # constant column: avoid division by zero
        return self                                        # returning self allows chaining

    def transform(self, X):
        check_is_fitted(self)
        X = validate_data(self, X, dtype=float, reset=False)   # reset=False: must match n_features_in_
        return (X - self.mean_) / self.scale_

    def inverse_transform(self, Z):
        check_is_fitted(self)
        return np.asarray(Z, dtype=float) * self.scale_ + self.mean_
