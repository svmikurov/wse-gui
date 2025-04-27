"""Provides mixins for MVC."""

from typing import Type

import toga

from wse.features.shared.observer import Subject


class CreateButtonMixin:
    """Mixin providing create button method."""

    subject: Subject
    BUTTON_CLASS: toga.Button

    # Utility methods
    def _create_button(
        self,
        button_cls: Type[toga.Button] | None = None,
        **kwargs: object,
    ) -> toga.Button:
        """Create a button to perform the model methods."""
        _cls = button_cls if button_cls is not None else self.BUTTON_CLASS
        return _cls(on_press=self._handle_button_press, **kwargs)

    # Notifications
    def _handle_button_press(self, button: toga.Button) -> None:
        """Handel button press."""
        self.subject.notify('handle_button_press', action=button.text)
