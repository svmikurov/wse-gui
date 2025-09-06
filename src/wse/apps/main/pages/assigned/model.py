"""Assigned exercise completion page model."""

from dataclasses import dataclass

from injector import inject

from wse.feature.base.model import ExerciseModel
from wse.feature.services import AssignedServiceProto
from wse.feature.shared.schemas.exercise import Assigned


@inject
@dataclass
class AssignedExerciseModel(
    ExerciseModel[Assigned, AssignedServiceProto],
):
    """Assigned exercise completion page model."""

    _exercise_service: AssignedServiceProto
