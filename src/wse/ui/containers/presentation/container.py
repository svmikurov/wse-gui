"""Presentation container layout."""

from dataclasses import dataclass

import toga
from injector import inject

from . import (
    PresentationContainerABC,
)


@inject
@dataclass
class PresentationContainer(
    PresentationContainerABC,
):
    """Presentaition container."""

    def _create_ui(self) -> None:
        self._case_panel = toga.Label('')
        self._text_panel = toga.Label('')

    def _populate_content(self) -> None:
        self._content.add(
            self._case_panel,
            self._text_panel,
        )

    def change_case(self, value: str) -> None:
        """Change case."""
        self._case_panel.text = value

    def change_text(self, value: str) -> None:
        """Change text."""
        self._text_panel.text = value
