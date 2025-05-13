"""Mathematical page package."""

from wse.features.mathem.pages.calculation_controller import (
    CalculationController,
)
from wse.features.mathem.pages.calculation_model import CalculationModel
from wse.features.mathem.pages.calculation_view import CalculationView
from wse.features.mathem.pages.mathem_controller import MathematicalController
from wse.features.mathem.pages.mathem_model import MathematicalModel
from wse.features.mathem.pages.mathem_view import MathematicalView

__all__ = [
    'CalculationModel',
    'CalculationController',
    'MathematicalController',
    'MathematicalModel',
    'MathematicalView',
    'CalculationView',
]
