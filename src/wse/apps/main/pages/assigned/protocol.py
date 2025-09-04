"""Defines protocol and ABC for Assigned exercise completion page."""

from typing import Protocol

from wse.apps.main.api.schema import ExerciseMeta
from wse.feature.base.model.exercise.protocol import ExerciseModelProto
from wse.feature.interfaces.imvc import ModelProto, PageControllerProto
from wse.feature.interfaces.imvc_exercise import ExerciseViewObserverProto


class AssignedModelProto(
    ModelProto,
    ExerciseModelProto[ExerciseMeta],
    Protocol,
):
    """Protocol for assigned exercise page model."""


class AssignedControllerProto(
    ExerciseViewObserverProto,
    PageControllerProto[ExerciseMeta],
    Protocol,
):
    """Protocol for Exercise completion page controller."""
