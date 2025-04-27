"""Defines Multiplication page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from wse.features.base.mvc import ContextController

if TYPE_CHECKING:
    from wse.features.mathem import MultiplicationModel, MultiplicationView

logger = logging.getLogger(__name__)


@dataclass
class MultiplicationController(ContextController):
    """Multiplication page controller."""

    model: MultiplicationModel
    view: MultiplicationView

    def on_open(self) -> None:
        """Perform events on page open."""
        self.model.lesson.start_lesson(listener=self)
        self.view.keypad.subscribe(self)

    # Listening to the model

    def display_task(self, value: str) -> None:
        """Display a task."""
        logger.debug(f'Displaying a task: {value}')
        self.view.text_inline_panel.change(value)

    # Listening to the view

    def check_answer(self, value: str) -> None:
        """Handel answer."""
        self.model.lesson.check_answer(value)

    # Keypad
    def handle_button(self, value: str) -> None:
        """Handel the button press."""
        logger.debug(f'Pressed button {value = }')
