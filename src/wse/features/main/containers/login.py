"""Defines login widgets container."""

from typing import Type, TypeVar

import toga
from toga.style import Pack

from wse.core.i18n import _
from wse.features.base.container import BaseContainer
from wse.features.shared.button import AppButton

WidgetType = TypeVar('WidgetType', bound=toga.Widget)


class LoginContainer(BaseContainer):
    """Login widgets container."""

    INPUT_HEIGHT = 60

    def __init__(self, *args: object, **kwarg: object) -> None:
        """Construct the container."""
        super().__init__(*args, **kwarg)

        # Add UI
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._username_input,
            self._password_input,
            self._btn_submit,
        )

    def _build_ui(self) -> None:
        self._username_input = self._build_input(toga.TextInput)
        self._password_input = self._build_input(toga.PasswordInput)
        self._btn_submit = AppButton(on_press=self._handel_submit)

    def localize_ui(self) -> None:
        """Update all UI elements with current translations."""
        self._username_input.placeholder = _('Username')
        self._password_input.placeholder = _('Password')
        self._btn_submit.text = _('Submit')

    # Button callback functions
    def _handel_submit(self, _: toga.Button) -> None:
        username = self._username_input.value
        password = self._password_input.value
        self.subject.notify(
            'submit_login', username=username, password=password
        )

    # Utility methods
    def _build_input(
        self,
        class_input: Type[WidgetType],
        **kwargs: object,
    ) -> WidgetType:
        return class_input(
            style=Pack(
                height=self.INPUT_HEIGHT,
            ),
            **kwargs,
        )
