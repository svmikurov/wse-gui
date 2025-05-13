"""Model layer implementation for widget components."""

import dataclasses
import logging
from typing import Callable

from toga.sources import Listener

from wse.features.shared.enums import FieldID
from wse.features.shared.enums.notify_id import NotifyID
from wse.features.shared.observer import IDSubject

logger = logging.getLogger(__name__)

NO_TEXT = ''


class KeypadChangeMixin:
    """Handles keypad input processing logic."""

    MAX_NUMBER_LENGTH = 3

    _text: str
    _notify_change: Callable[[], None]

    def change(self, value: str) -> None:
        """Update text based on keypad input."""
        if value == '⌫' and self._text == '0.':
            self._text = NO_TEXT
        elif value == '⌫':
            self._text = self._text[:-1]
        elif len(self._text) >= self.MAX_NUMBER_LENGTH:
            return
        elif value == '.' and value in self._text:
            return
        elif value == '.' and self._text == NO_TEXT:
            self._text += '0.'
        elif self._text == '0':
            self._text += '.' + value
        else:
            self._text += value

        self._notify_change()


class ChangeMixin:
    """Basic text change handling."""

    _text: str
    _notify_change: Callable[[], None]

    def change(self, value: str) -> None:
        """Update the text value and notify subscribers."""
        self._text = value
        self._notify_change()


@dataclasses.dataclass
class BaseDisplayModel:
    """Base model for display components with notification support."""

    _subject: IDSubject
    _text: str = NO_TEXT
    _field: FieldID = NO_TEXT

    def clean(self) -> None:
        """Clear text and notify subscribers."""
        self._text = NO_TEXT
        self._notify_clean()

    # Notifications

    def _notify_change(self) -> None:
        """Notify about text changes."""
        self.subject.notify_with_id(
            notify_id=NotifyID.UI_FIELD_VALUE_UPDATED,
            field_id=self._field,
            value=self._text,
        )

    def _notify_clean(self) -> None:
        """Notify about text clearance."""
        self.subject.notify_with_id(
            notify_id=NotifyID.UI_FIELD_CLEARED,
            field_id=self._field,
        )

    # Utility methods

    @property
    def subject(self) -> IDSubject:
        """Model subject."""
        return self._subject

    @property
    def text(self) -> str:
        """Display model text."""
        return self._text

    def subscribe(self, field: FieldID, listener: Listener) -> None:
        """Subscribe a listener to model changes with UI name."""
        self._field = field
        self.subject.add_listener(listener=listener)


class DisplayModel(ChangeMixin, BaseDisplayModel):
    """Model for managing display text and notifying subscribers."""


class KeypadModel(KeypadChangeMixin, BaseDisplayModel):
    """Combines keypad input processing with display management."""

    _subject: IDSubject
