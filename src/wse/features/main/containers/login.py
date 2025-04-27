"""Defines login widgets container."""

import logging
from typing import Type, TypeVar

import toga
from toga import validators
from toga.style import Pack

from wse.core.i18n import _
from wse.features.base.container import BaseContainer
from wse.features.shared.ui.button import AppButton

WidgetType = TypeVar('WidgetType', bound=toga.Widget)

MAX_USER_LENGTH = 150
MIN_USER_LENGTH = 3
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 150

BLANK = ''

logger = logging.getLogger(__name__)


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

    def _create_ui(self) -> None:
        self._username_input = self._build_input(
            toga.TextInput,
            validators=[
                validators.LengthBetween(
                    MIN_USER_LENGTH,
                    MAX_USER_LENGTH,
                    error_message=f'Please enter from {MIN_USER_LENGTH}'
                    f' to {MAX_USER_LENGTH} characters',
                    allow_empty=False,
                ),
            ],
        )
        self._password_input = self._build_input(
            toga.PasswordInput,
            validators=[
                validators.LengthBetween(
                    MIN_PASSWORD_LENGTH,
                    MAX_PASSWORD_LENGTH,
                    error_message=f'Please enter from {MIN_PASSWORD_LENGTH}'
                    f' to {MAX_PASSWORD_LENGTH} characters',
                    allow_empty=False,
                ),
            ],
        )
        self._btn_submit = AppButton(on_press=self._handel_submit)

    def localize_ui(self) -> None:
        """Update all UI elements with current translations."""
        self._username_input.placeholder = _('Username')
        self._password_input.placeholder = _('Password')
        self._btn_submit.text = _('Submit')

    def clear_input_fields(self) -> None:
        """Clear a username and password fields."""
        self._username_input.value = BLANK
        self._password_input.value = BLANK

    # Button callback functions
    def _handel_submit(self, _: toga.Button) -> None:
        username = self._username_input.value
        password = self._password_input.value

        # Check that all fields are filled
        if username and password:
            self._notify_submit(username, password)
        else:
            logger.info('Fill all the fields of forms')

    # Build methods
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

    # Notifications
    def _notify_submit(self, username: str, password: str) -> None:
        self.subject.notify(
            'submit_login', username=username, password=password
        )
