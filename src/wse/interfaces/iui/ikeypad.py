"""Defines protocol interfaces for keypad."""

from typing import Protocol

import toga

from wse.interfaces.ifeatures.isubjects import IModelSubject

# fmt: off


class IKeypadModel(Protocol):
    """Model for managing display text and notifying subscribers."""

    _subject: IModelSubject
    _text: str = ''

    def change(self, value: str) -> None:
        """Process input value and update displayed text."""
    def clear(self) -> None:
        """Reset text to empty string and notify subscribers."""
    def _notify_change(self) -> None: ...
    def _notify_clean(self) -> None: ...
    @property
    def subject(self) -> IModelSubject:
        """Model subject."""
    @property
    def text(self) -> str: ...
    def add_listener(self, listener: object) -> None: ...


class IKeypad(Protocol):
    """Protocol defining the interface for keypad."""
    @property
    def content(self) -> [toga.Widget]:
        """Widgets of keypad."""
    def add_listener(self, listener: object) -> None:
        """Register an observer to receive notifications."""
