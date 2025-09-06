"""Simple Math calculation page controller."""

from dataclasses import dataclass

from injector import inject

from wse.apps.math.api import Calculation
from wse.feature.base.mvc import PageController
from wse.feature.base.mvc_exercise import ExerciseViewObserver
from wse.feature.interfaces.imvc_exercise import ExerciseModelFeatureProto
from wse.feature.shared.views import IntegerViewProto

from .protocol import CalculationModelProto


@inject
@dataclass
class CalculationController(
    ExerciseViewObserver[ExerciseModelFeatureProto],
    PageController[
        CalculationModelProto,
        IntegerViewProto,
        Calculation,
    ],
):
    """Simple Math calculation page controller."""

    _model: CalculationModelProto
    _view: IntegerViewProto

    def on_open(self, value: Calculation | None = None) -> None:
        """Call methods when page opens."""
        if not isinstance(value, Calculation):
            raise TypeError(
                f'Expected Calculation type, got {type(value).__name__}'
            )
        self._model.set_exercise(value)
