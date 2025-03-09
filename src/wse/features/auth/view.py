"""Defines the login screen view."""

import toga
from toga.constants import CENTER
from toga.style import Pack

from wse.features.shared.ui.box import ColumnFlexBox
from wse.utils.i18n import _


class LoginView(ColumnFlexBox):
    """Represents the login screen."""

    def __init__(self) -> None:
        """Initialize the view."""
        super().__init__()
        self._setup_styles()
        self._create_widgets()
        self._add_widgets_to_view()

    def _setup_styles(self) -> None:
        """Define styles for widgets."""
        self.FONT_SIZE = 20
        self.HEADING_PADDING_TOP = 30
        self.HEADING_PADDING_BOTTOM = 10
        self.INPUT_PADDING_TOP = 10
        self.SUBMIT_PADDING_TOP = 20

        self.general_style = {
            'padding_right': 25,
            'padding_left': 25,
            'font_size': self.FONT_SIZE,
            'height': 70,
        }

    def _create_widgets(self) -> None:
        """Create widgets for the login screen."""
        self.heading = toga.Label(
            text=_('Login'),
            style=Pack(
                padding_top=self.HEADING_PADDING_TOP,
                padding_bottom=self.HEADING_PADDING_BOTTOM,
                text_align=CENTER,
                font_size=self.FONT_SIZE,
            ),
        )
        self.username_input = toga.TextInput(
            placeholder=_('Username'),
            style=Pack(
                padding_top=self.INPUT_PADDING_TOP, **self.general_style
            ),
        )
        self.password_input = toga.PasswordInput(
            placeholder=_('Password'),
            style=Pack(
                padding_top=self.INPUT_PADDING_TOP, **self.general_style
            ),
        )
        self.submit_button = toga.Button(
            text=_('Login submit'),
            style=Pack(
                padding_top=self.SUBMIT_PADDING_TOP, **self.general_style
            ),
            on_press=self._on_login_click,
        )

    def _add_widgets_to_view(self) -> None:
        """Add widgets to the view."""
        self.add(
            self.heading,
            self.username_input,
            self.password_input,
            self.submit_button,
        )

    def _on_login_click(self, _: toga.Widget) -> None:
        self.notify('handel_login')

    @property
    def username(self) -> str:
        """Return username."""
        return self.username_input.value

    @property
    def password(self) -> str:
        """Return password."""
        return self.password_input.value
