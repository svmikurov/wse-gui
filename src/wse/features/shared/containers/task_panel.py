"""Defines base  and base abstract class for common view containers."""

from dataclasses import dataclass
from typing import Type

import toga
from injector import inject

from wse.config.layout import TextTaskStyle, TextTaskTheme

from ...base.container import BaseContainer
from ...shared.widgets.interfaces import IDivider


@inject
@dataclass
class TextTaskPanel(
    BaseContainer,
):
    """Abstract base class for I/O one line text container."""

    _divider: Type[IDivider]
    _style_config: TextTaskStyle
    _theme_config: TextTaskTheme

    def _setup(self) -> None:
        self.update_style(self._style_config)
        self.update_style(self._theme_config)

    def _populate_content(self) -> None:
        self.content.add(
            self._label_question,
            self._divider(),
            self._label_answer,
        )

    def _create_ui(self) -> None:
        self._label_question = toga.Label('')
        self._label_answer = toga.Label('')

    # Fields control methods

    def display_question(self, value: str) -> None:
        """Update the output text field."""
        self._label_question.text = value

    def clear_question(self) -> None:
        """Clear the output text field."""
        self._label_question.text = ''

    def display_answer(self, value: str) -> None:
        """Update the input text field."""
        self._label_answer.text = value

    def clear_answer(self) -> None:
        """Clear the input text field."""
        self._label_answer.text = ''

    def localize_ui(self) -> None:
        """Localize the UI text."""

    def update_style(self, config: TextTaskStyle | TextTaskTheme) -> None:
        """Update widgets style."""
        self._label_question.style.update(**config.label_question)
        self._label_answer.style.update(**config.label_answer)
