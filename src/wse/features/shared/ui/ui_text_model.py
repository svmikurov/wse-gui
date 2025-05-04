"""Defines model for widgets."""

import dataclasses
from typing import Callable

from wse.features.shared.enums import UIName
from wse.interface.iobserver import ISubject


class KeypadModelMixin:
    """Mixin providing keypad input processing logic."""

    _text: str
    _notify_change: Callable[[], None]

    def change(self, value: str) -> None:
        """Process input value and update displayed text."""
        if value == '⌫' and self._text == '0.':
            self._text = ''
        elif value == '⌫':
            self._text = self._text[:-1]
        elif value == '.' and value in self._text:
            return
        elif value == '.' and self._text == '':
            self._text += '0.'
        elif value == '0' and self._text == '':
            self._text += '0.'
        else:
            self._text += value
        self._notify_change()


@dataclasses.dataclass
class DisplayModel:
    """Model for managing display text and notifying subscribers."""

    _subject: ISubject
    _text: str = ''
    _ui_name: UIName = ''

    def change(self, value: str) -> None:
        """Update the displayed text and notify subscribers."""
        self._text = value
        self._notify_change()

    def clean(self) -> None:
        """Reset text to empty string and notify subscribers."""
        self._text = ''
        self._notify_clean()

    # Notifications

    def _notify_change(self) -> None:
        self.subject.notify(
            'change_ui_value', ui_name=self._ui_name, value=self._text
        )

    def _notify_clean(self) -> None:
        self.subject.notify('clean_ui_value', ui_name=self._ui_name)

    # Utility methods

    @property
    def subject(self) -> ISubject:
        """Model subject."""
        return self._subject

    @property
    def text(self) -> str:
        """Display model text."""
        return self._text

    def subscribe(self, ui_name: UIName, listener: object) -> None:
        """Subscribe a listener to model changes with UI name."""
        self._ui_name = ui_name
        self.subject.add_listener(listener=listener)


class KeypadModel(KeypadModelMixin, DisplayModel):
    """Combines keypad input processing with display management."""
