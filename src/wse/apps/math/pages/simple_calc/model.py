"""Simple Math calculation page model."""

from dataclasses import dataclass

from injector import inject

from wse.apps.main.api.schema import ExerciseMeta
from wse.feature.base.model import ExerciseModel
from wse.feature.services import CalculationServiceProto


@inject
@dataclass
class CalculationModel(
    ExerciseModel[ExerciseMeta, CalculationServiceProto],
):
    """Simple Math calculation page model."""

    _exercise_service: CalculationServiceProto
