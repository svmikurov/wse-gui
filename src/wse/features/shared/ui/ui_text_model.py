"""Defines model for widgets."""

import dataclasses

from wse.features.shared.enums import UIName
from wse.interface.iobserver import ISubject


@dataclasses.dataclass
class DisplayModel:
    """Model providing processing of text panel."""

    _subject: ISubject
    _text: str = ''
    _ui_name: UIName = ''

    def change(self, value: str) -> None:
        """Change a text to display."""
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
        self._change_display_text()

    def clean(self) -> None:
        """Clean a text in display panel."""
        self._text = ''
        self._notify_clean()

    def _change_display_text(self) -> None:
        self._notify_change()

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

    def set_ui_name(self, ui_name: UIName) -> None:
        """Set ui name for notifications."""
        self._ui_name = ui_name
