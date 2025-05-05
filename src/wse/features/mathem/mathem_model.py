"""Defines Mathematical model."""

import logging

from toga.sources import Listener

from wse.features.base.mvc import BaseModel

logger = logging.getLogger(__name__)


class MathematicalModel(BaseModel, Listener):
    """Mathematical page model."""

    def __init__(self, *, exercise_switcher, **kwargs):
        super().__init__(**kwargs)
        self._switcher = exercise_switcher
        self._current_exercise = None
        self.refresh_exercise()

    def set_exercise_type(self, exercise_type: str):
        self._switcher.set_exercise_type(exercise_type)
        self.refresh_exercise()

    def refresh_exercise(self):
        self._current_exercise = self._switcher.get_exercise()
