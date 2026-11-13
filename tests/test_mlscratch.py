"""Tests for mlscratch. Run from the repo root with:  python -m pytest -q"""
import numpy as np
import pytest
from sklearn.base import clone
from sklearn.decomposition import PCA
from sklearn.exceptions import NotFittedError
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

from mlscratch import LinearRegressionScratch, PCAScratch, StandardScalerScratch, mean_squared_error


@pytest.fixture
def data():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 4)) * [1, 10, 0.1, 5] + [0, 50, -3, 2]
    w = np.array([2.0, -0.5, 7.0, 0.3])
    y = X @ w + 4 + rng.normal(0, 0.1, size=200)
    return X, y


# ---------- scaler ----------
def test_scaler_matches_sklearn(data):
    X, _ = data
    np.testing.assert_allclose(StandardScalerScratch().fit_transform(X), StandardScaler().fit_transform(X))


def test_scaler_inverse_roundtrip(data):
    X, _ = data
    s = StandardScalerScratch().fit(X)
    np.testing.assert_allclose(s.inverse_transform(s.transform(X)), X)


def test_scaler_constant_column_no_nan():
    X = np.c_[np.ones(10), np.arange(10.0)]
    assert np.isfinite(StandardScalerScratch().fit_transform(X)).all()


# ---------- linear regression ----------
@pytest.mark.parametrize("solver", ["normal", "gd"])
def test_linreg_matches_sklearn(data, solver):
    X, y = data
    Xs = StandardScaler().fit_transform(X)                 # GD converges fast on scaled data
    ours = LinearRegressionScratch(solver=solver).fit(Xs, y)
    ref = LinearRegression().fit(Xs, y)
    np.testing.assert_allclose(ours.coef_, ref.coef_, rtol=1e-6, atol=1e-6)
    assert ours.intercept_ == pytest.approx(ref.intercept_, rel=1e-6)


def test_gd_diverges_with_too_large_step(data):
    X, y = data
    Xs = StandardScaler().fit_transform(X)
    L = 2 / len(Xs) * np.linalg.norm(np.c_[np.ones(len(Xs)), Xs], 2) ** 2
    with pytest.raises(FloatingPointError):
        LinearRegressionScratch(solver="gd", lr=2.2 / L, max_iter=20000).fit(Xs, y)


def test_predict_before_fit_raises():
    with pytest.raises(NotFittedError):
        LinearRegressionScratch().predict(np.zeros((2, 3)))


def test_clone_and_get_params():
    m = LinearRegressionScratch(solver="gd", lr=0.01)
    c = clone(m)
    assert c.get_params() == m.get_params() and c is not m


def test_wrong_number_of_features(data):
    X, y = data
    m = LinearRegressionScratch().fit(X, y)
    with pytest.raises(ValueError):
        m.predict(X[:, :2])


# ---------- PCA ----------
def test_pca_matches_sklearn_up_to_sign(data):
    X, _ = data
    ours = PCAScratch(n_components=3).fit(X)
    ref = PCA(n_components=3).fit(X)
    np.testing.assert_allclose(ours.explained_variance_ratio_, ref.explained_variance_ratio_)
    np.testing.assert_allclose(np.abs(ours.components_), np.abs(ref.components_), atol=1e-10)


def test_pca_full_reconstruction(data):
    X, _ = data
    p = PCAScratch().fit(X)
    np.testing.assert_allclose(p.inverse_transform(p.transform(X)), X)


# ---------- metrics ----------
def test_mse():
    assert mean_squared_error([1, 2, 3], [1, 2, 5]) == pytest.approx(4 / 3)
    with pytest.raises(ValueError):
        mean_squared_error([1, 2], [1, 2, 3])
