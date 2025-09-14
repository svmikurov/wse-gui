"""Defines I/O text container."""

from dataclasses import dataclass
from typing import Type

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig

from ...base.container import AddContentABC
from ...shared.widgets import DividerProto
from . import TextTaskContainerProto


@inject
@dataclass
class TextTaskPanel(
    AddContentABC,
    TextTaskContainerProto,
):
    """I/O text container."""

    _divider: Type[DividerProto]
    _style: StyleConfig
    _theme: ThemeConfig

    def _setup(self) -> None:
        self.update_style(self._style)
        self.update_style(self._theme)

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

    def display_correct_answer(self, expression: str) -> None:
        """Display the correct answer."""
        self.display_question(expression)

    def localize_ui(self) -> None:
        """Localize the UI text."""

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_question.style.update(**config.text_task.label_question)
        self._label_answer.style.update(**config.text_task.label_answer)

    @property
    def answer(self) -> str:
        """Get text."""
        answer: str = self._label_answer.text
        return answer
