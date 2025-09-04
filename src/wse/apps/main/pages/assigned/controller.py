"""Simple Math calculation page controller."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.apps.main.api.schema import ExerciseMeta
from wse.feature.base.mvc import PageController
from wse.feature.base.mvc_exercise import ExerciseViewObserver
from wse.feature.interfaces.imvc_exercise import ExerciseModelFeatureProto
from wse.feature.shared.views import IntegerViewProto

from .protocol import AssignedModelProto


@inject
@dataclass
class AssignedController(
    ExerciseViewObserver[ExerciseModelFeatureProto],
    PageController[
        AssignedModelProto,
        IntegerViewProto,
        ExerciseMeta,
    ],
):
    """Simple Math calculation page controller."""

    _model: AssignedModelProto
    _view: IntegerViewProto

    @override
    def on_open(self, value: ExerciseMeta | None = None) -> None:
        """Call methods when page opens."""
        if not isinstance(value, ExerciseMeta):
            raise TypeError(
                f'Expected ExerciseMeta type, got {type(value).__name__}'
            )
        self._model.set_exercise(value)
