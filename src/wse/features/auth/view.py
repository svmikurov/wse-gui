"""Defines the login screen view."""

import toga
from toga.constants import CENTER
from toga.style import Pack

from wse.core.i18n import I18NService
from wse.features.shared.observer import Subject
from wse.features.shared.ui.box import ColumnFlexBox


class LoginView(ColumnFlexBox, Subject):
    """Represents the login screen."""

    def __init__(self, i18n_service: I18NService) -> None:
        """Construct the view."""
        super().__init__()
        Subject.__init__(self)
        # Initializing the translation service
        self.i18n = i18n_service
        self.i18n.add_listener(self)  # Subscribe to change language
        self._ = self.i18n.gettext  # Abbreviation for translation method

        # Creating interface components
        self._setup_styles()
        self._create_ui()
        self._add_ui_to_view()
        self.update_ui_texts()  # Initial installation of texts

    def _setup_styles(self) -> None:
        """Define styles for UI."""
        self.FONT_SIZE = 20
        self.HEADING_PADDING_TOP = 30
        self.HEADING_PADDING_BOTTOM = 20
        self.INPUT_PADDING_TOP = 10
        self.SUBMIT_PADDING_TOP = 20

        self.general_style = {
            'padding_right': 25,
            'padding_left': 25,
            'font_size': self.FONT_SIZE,
            'height': 70,
        }

    def _create_ui(self) -> None:
        """Create UI for the login screen."""
        self.heading = toga.Label(
            '',
            style=Pack(
                padding_top=self.HEADING_PADDING_TOP,
                padding_bottom=self.HEADING_PADDING_BOTTOM,
                text_align=CENTER,
                font_size=self.FONT_SIZE,
            ),
        )
        self.username_input = toga.TextInput(
            style=Pack(**self.general_style),
        )
        self.password_input = toga.PasswordInput(
            style=Pack(
                padding_top=self.INPUT_PADDING_TOP, **self.general_style
            ),
        )
        self.submit_button = toga.Button(
            style=Pack(
                padding_top=self.SUBMIT_PADDING_TOP, **self.general_style
            ),
            on_press=self._on_login_click,
        )

    def _add_ui_to_view(self) -> None:
        self.add(
            self.heading,
            self.username_input,
            self.password_input,
            self.submit_button,
        )

    def update_ui_texts(self) -> None:
        """Update all UI elements with current translations."""
        self.heading.text = self._('Login')
        self.username_input.placeholder = self._('Username')
        self.password_input.placeholder = self._('Password')
        self.submit_button.text = self._('Login submit')

    ####################################################################
    # Button handlers

    async def _on_login_click(self, _: toga.Widget) -> None:
        await self.notify_async(
            'handle_login',
            username=self.username_input.value,
            password=self.password_input.value,
        )
