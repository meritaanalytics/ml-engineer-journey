"""PCA from scratch (Lesson 2), via SVD of the centred data."""
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted, validate_data


class PCAScratch(TransformerMixin, BaseEstimator):
    """Principal Component Analysis.

    Parameters
    ----------
    n_components : int or None, default=None
        Number of components to keep (None = all).

    Attributes
    ----------
    components_ : ndarray (n_components, n_features)  - principal directions (rows)
    explained_variance_ : ndarray (n_components,)      - eigenvalues of the covariance matrix
    explained_variance_ratio_ : ndarray (n_components,)
    mean_ : ndarray (n_features,)
    """

    def __init__(self, n_components=None):
        self.n_components = n_components

    def fit(self, X, y=None):
        X = validate_data(self, X, dtype=float, ensure_min_samples=2)
        n, d = X.shape
        k = min(n, d) if self.n_components is None else self.n_components
        if not 1 <= k <= min(n, d):
            raise ValueError(f"n_components must be between 1 and {min(n, d)}, got {k}")
        self.mean_ = X.mean(axis=0)
        U, S, Vt = np.linalg.svd(X - self.mean_, full_matrices=False)
        # deterministic signs: the largest-|loading| entry of each component is positive
        signs = np.sign(Vt[np.arange(len(Vt)), np.argmax(np.abs(Vt), axis=1)])
        signs[signs == 0] = 1
        Vt = Vt * signs[:, None]
        var = S ** 2 / (n - 1)
        total = var.sum() if var.sum() > 0 else 1.0
        self.components_ = Vt[:k]
        self.explained_variance_ = var[:k]
        self.explained_variance_ratio_ = var[:k] / total
        self.n_components_ = k
        return self

    def transform(self, X):
        check_is_fitted(self)
        X = validate_data(self, X, dtype=float, reset=False)
        return (X - self.mean_) @ self.components_.T

    def inverse_transform(self, T):
        check_is_fitted(self)
        return np.asarray(T, dtype=float) @ self.components_ + self.mean_
