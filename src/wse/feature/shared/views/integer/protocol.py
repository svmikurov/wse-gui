"""Protocol for Exercise view with integer I/O UI."""

from typing import Protocol

from wse.feature.interfaces.imvc import ViewProto
from wse.feature.interfaces.imvc_exercise import (
    ExerciseModelObserverProto,
    ExerciseViewObserverProto,
)


class IntegerViewObserverProto(
    ExerciseModelObserverProto,
    Protocol,
):
    """Protocol for observe to notifications."""


class IntegerViewProto(
    ViewProto,
    Protocol,
):
    """Protocol for Exercise view with integer I/O UI interface."""


class IntegerViewNotifyProto(
    ExerciseViewObserverProto,
    Protocol,
):
    """Protocol for Integer view event observer interface."""
