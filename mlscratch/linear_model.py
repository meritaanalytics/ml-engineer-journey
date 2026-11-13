"""Linear regression from scratch (Lesson 1: predict, MSE, gradient)."""
import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.utils.validation import check_is_fitted, validate_data


class LinearRegressionScratch(RegressorMixin, BaseEstimator):
    """Ordinary least squares, solved two ways.

    Parameters
    ----------
    solver : {"normal", "gd"}, default="normal"
        "normal": least squares via SVD (np.linalg.lstsq), exact, O(n d^2).
        "gd": batch gradient descent on the MSE (iterative; scales to models without a closed form).
    lr : float or None, default=None
        Gradient-descent step size. None -> 1/L, where L is the largest eigenvalue of the
        MSE Hessian (2/n) A^T A, which guarantees convergence (any lr < 2/L converges).
    max_iter : int, default=5000
    tol : float, default=1e-10
        Stop when the relative improvement in loss falls below tol.
    fit_intercept : bool, default=True

    Attributes
    ----------
    coef_ : ndarray (n_features,)
    intercept_ : float
    n_iter_ : int                 - gradient-descent iterations used (1 for "normal")
    loss_history_ : list[float]   - MSE at each iteration (empty for "normal")
    """

    def __init__(self, solver="normal", lr=None, max_iter=5000, tol=1e-10, fit_intercept=True):
        self.solver = solver
        self.lr = lr
        self.max_iter = max_iter
        self.tol = tol
        self.fit_intercept = fit_intercept

    def _design(self, X):
        """Bias trick: prepend a column of ones so the intercept is weight w[0]."""
        return np.c_[np.ones(len(X)), X] if self.fit_intercept else X

    def fit(self, X, y):
        X, y = validate_data(self, X, y, dtype=float, y_numeric=True)
        A = self._design(X)
        if self.solver == "normal":
            w, *_ = np.linalg.lstsq(A, y, rcond=None)      # stable (SVD-based), never an explicit inverse
            self.n_iter_, self.loss_history_ = 1, []          # one exact "step"
        elif self.solver == "gd":
            w, self.loss_history_, self.n_iter_, self.lr_ = self._gradient_descent(A, y)
        else:
            raise ValueError(f"solver must be 'normal' or 'gd', got {self.solver!r}")
        if self.fit_intercept:
            self.intercept_, self.coef_ = float(w[0]), w[1:]
        else:
            self.intercept_, self.coef_ = 0.0, w
        return self

    def _gradient_descent(self, A, y):
        n = len(A)
        L = 2.0 / n * np.linalg.norm(A, 2) ** 2            # largest eigenvalue of the Hessian (2/n) A^T A
        lr = self.lr if self.lr is not None else (1.0 / L if L > 0 else 1.0)
        w = np.zeros(A.shape[1])
        history = []
        with np.errstate(over="ignore", invalid="ignore"):  # divergence is detected and reported below
            for it in range(self.max_iter):
                r = A @ w - y
                loss = r @ r / n
                history.append(float(loss))
                if not np.isfinite(loss):
                    raise FloatingPointError(
                        f"gradient descent diverged at iteration {it}: lr={lr:.3g} exceeds 2/L={2 / L:.3g}")
                if it > 0 and abs(history[-2] - loss) <= self.tol * max(history[-2], 1e-300):
                    break
                w = w - lr * (2.0 / n) * (A.T @ r)          # w <- w - lr * gradient
        return w, history, it + 1, lr

    def predict(self, X):
        check_is_fitted(self)
        X = validate_data(self, X, dtype=float, reset=False)
        return X @ self.coef_ + self.intercept_
