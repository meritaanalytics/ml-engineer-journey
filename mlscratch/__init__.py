"""mlscratch: machine-learning algorithms built from first principles with NumPy,
following the scikit-learn estimator API so they plug into Pipelines, cross-validation
and grid search.

Built during the ML Engineer Journey by Benson M. Merita.
"""
from .preprocessing import StandardScalerScratch
from .linear_model import LinearRegressionScratch
from .decomposition import PCAScratch
from .metrics import mean_squared_error

__version__ = "0.1.0"
__all__ = ["StandardScalerScratch", "LinearRegressionScratch", "PCAScratch", "mean_squared_error"]
