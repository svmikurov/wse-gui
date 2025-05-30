"""Model layer implementation for widget components."""

import dataclasses

from toga.sources import Listener

from wse.interfaces.iobserver import ISubject

NO_TEXT = ''


@dataclasses.dataclass
class BaseDisplayModel:
    """Base model for display components with notification support."""

    _subject: ISubject
    _text: str = NO_TEXT

    # Observer management

    def add_listener(self, listener: Listener) -> None:
        """Subscribe a listener to model."""
        self.subject.add_listener(listener=listener)

    # Notifications

    def clear(self) -> None:
        """Clear the widget value."""
        self.subject.notify('clear')

    # Utility methods

    @property
    def subject(self) -> ISubject:
        """Model subject."""
        return self._subject

    @property
    def text(self) -> str:
        """Display model text."""
        return self._text


class DisplayModel(BaseDisplayModel):
    """Model for managing display text and notifying subscribers."""

    def change(self, value: str) -> None:
        """Update the text value and notify subscribers."""
        self._text = value
        self.subject.notify('change', value=value)


class KeypadModel(BaseDisplayModel):
    """Combines keypad input processing with display management."""

    MAX_NUMBER_LENGTH = 9

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

        self.subject.notify('change', value=self._text)
