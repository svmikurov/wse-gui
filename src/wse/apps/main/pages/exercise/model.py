"""Defines Exercise completion page model."""

from dataclasses import dataclass

from injector import inject

from wse.apps.main.pages.exercise.iabc import ExerciseModelABC

from ...http.dto import ExerciseMetaDTO


@inject
@dataclass
class ExerciseModel(
    ExerciseModelABC,
):
    """Exercise completion page model."""

    def on_open(self, meta: ExerciseMetaDTO) -> None:
        """Call methods when page opens."""
        print('-----------------------------')
        print(f'{meta = }')
        print('-----------------------------')
