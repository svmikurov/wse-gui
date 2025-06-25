"""Defines base  and base abstract class for common view containers."""

from abc import ABC
from dataclasses import dataclass

import toga

from wse.features.base.container import BaseContainer


@dataclass
class BaseTextIOContainer(
    BaseContainer,
    ABC,
):
    """Abstract base class for I/O one line text container."""

    def _populate_content(self) -> None:
        self.content.add(
            self._output_label,
            self._output_text,
            self._input_label,
            self._input_text,
        )

    def _create_ui(self) -> None:
        self._output_label = toga.Label('')
        self._output_text = toga.Label('')
        self._input_label = toga.Label('')
        self._input_text = toga.Label('')

    # Fields control methods

    def display_output(self, text: str) -> None:
        """Update the output text field."""
        self._output_text.text = text

    def clear_output(self) -> None:
        """Clear the output text field."""
        self._output_text.text = ''

    def display_input(self, text: str) -> None:
        """Update the input text field."""
        self._input_text.text = text

    def clear_input(self) -> None:
        """Clear the input text field."""
        self._input_text.text = ''
