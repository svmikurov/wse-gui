"""Defines protocols for Simple Math Calculation page components."""

from typing import Protocol

from wse.apps.math.api import Calculation
from wse.feature.base.model.exercise.protocol import ExerciseModelProto
from wse.feature.interfaces.imvc import ModelProto, PageControllerProto
from wse.feature.interfaces.imvc_exercise import ExerciseViewObserverProto


class CalculationModelProto(
    ExerciseModelProto[Calculation],
    ModelProto,
    Protocol,
):
    """Simple math calculation page view."""


class CalculationControllerProto(
    PageControllerProto[Calculation],
    ExerciseViewObserverProto,
    Protocol,
):
    """The controller of Simple Math calculation page."""
