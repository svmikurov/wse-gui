"""Defines protocol interfaces for keypad."""

from typing import Protocol

import toga

from wse.features.shared.enums import FieldID
from wse.interfaces.ifeatures.isubjects import IModelSubject

# fmt: off


class IKeypadModel(Protocol):
    """Model for managing display text and notifying subscribers."""

    _subject: IModelSubject
    _text: str = ''
    _field: FieldID = ''

    def change(self, value: str) -> None:
        """Process input value and update displayed text."""
    def clean(self) -> None:
        """Reset text to empty string and notify subscribers."""
    def _notify_change(self) -> None: ...
    def _notify_clean(self) -> None: ...
    @property
    def subject(self) -> IModelSubject:
        """Model subject."""
    @property
    def text(self) -> str: ...
    def subscribe(self, field: FieldID, listener: object) -> None: ...


class IKeypad(Protocol):
    """Protocol defining the interface for keypad."""
    @property
    def content(self) -> [toga.Widget]:
        """Widgets of keypad."""
    def subscribe(self, listener: object) -> None:
        """Register an observer to receive notifications."""
