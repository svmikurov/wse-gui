"""Manages the logic for the main feature."""

from __future__ import annotations

from typing import TYPE_CHECKING

from toga.sources import Listener

from wse.core.logger import setup_logger
from wse.features.exercise.model import ExerciseModel
from wse.features.exercise.view import ExercisesView

if TYPE_CHECKING:
    from wse.core.navigation.navigator import Navigator

logger = setup_logger('ExerciseController')


class ExerciseController(Listener):
    """Exercise screen controller."""

    def __init__(
        self,
        model: ExerciseModel,
        view: ExercisesView,
        navigator: Navigator,
    ) -> None:
        """Construct the controller."""
        self.model = model
        self.view = view
        self.navigator = navigator
        self.view.subject.add_listener(self)

    def back(self) -> None:
        """Handel back button press event."""
        self.navigator.back()
