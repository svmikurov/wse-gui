"""Protocol for exercise page model."""

from typing import Any, Protocol, TypeVar

from wse.apps.main.api.schema import ExerciseMeta
from wse.feature.services import ExerciseServiceProto

ExerciseT_contra = TypeVar(
    'ExerciseT_contra',
    contravariant=True,
    bound=ExerciseMeta,
)
"""Exercise type to pass to the `on_open` method.
"""

ServiceT = TypeVar(
    'ServiceT',
    bound=ExerciseServiceProto[Any],
)
"""Service type for exercise completion.
"""


class ExerciseModelProto(Protocol[ExerciseT_contra]):
    """Protocol for Exercise page model interface."""

    def set_exercise(self, exercise: ExerciseT_contra) -> None:
        """Set the exercise with and it conditions."""

    def update_task(self) -> None:
        """Start or update task."""

    def set_answer(self, value: str) -> None:
        """Set the entered user answer."""

    def check_answer(self) -> None:
        """Check the user's submitted answer."""
