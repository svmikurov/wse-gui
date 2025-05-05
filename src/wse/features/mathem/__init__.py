"""Mathematical page package."""

from wse.features.mathem.calculation_controller import (
    CalculationController,
)
from wse.features.mathem.calculation_model import CalculationModel
from wse.features.mathem.calculation_view import CalculationView
from wse.features.mathem.mathem_controller import MathematicalController
from wse.features.mathem.mathem_model import MathematicalModel
from wse.features.mathem.mathem_view import MathematicalView

__all__ = [
    'CalculationModel',
    'CalculationController',
    'MathematicalController',
    'MathematicalModel',
    'MathematicalView',
    'CalculationView',
]
