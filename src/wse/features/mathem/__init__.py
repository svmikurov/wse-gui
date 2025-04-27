"""Mathematical page package."""

from wse.features.mathem.mathem_controller import MathematicalController
from wse.features.mathem.mathem_model import MathematicalModel
from wse.features.mathem.mathem_view import MathematicalView
from wse.features.mathem.multiplication_controller import (
    MultiplicationController,
)
from wse.features.mathem.multiplication_model import MultiplicationModel
from wse.features.mathem.multiplication_view import MultiplicationView

__all__ = [
    'MathematicalController',
    'MathematicalModel',
    'MathematicalView',
    'MultiplicationController',
    'MultiplicationModel',
    'MultiplicationView',
]
