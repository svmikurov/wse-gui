"""Defines Exercise completion page controller."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from ...http.dto import ExerciseMetaDTO
from .iabc import ExerciseControllerABC, IExerciseModel, IExerciseView


@inject
@dataclass
class ExerciseController(
    ExerciseControllerABC,
):
    """Exercise completion page controller."""

    _model: IExerciseModel
    _view: IExerciseView

    @override
    def on_open(self, meta: ExerciseMetaDTO) -> None:  # type: ignore[override]
        """Call methods when page opens."""
        self._model.on_open(meta)
