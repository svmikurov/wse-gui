"""Assigned exercise completion page model."""

from dataclasses import dataclass

from injector import inject

from wse.apps.main.api.schema import Assigned
from wse.feature.base.model import ExerciseModel
from wse.feature.services import AssignedServiceProto


@inject
@dataclass
class AssignedExerciseModel(
    ExerciseModel[Assigned, AssignedServiceProto],
):
    """Assigned exercise completion page model."""

    _exercise_service: AssignedServiceProto
