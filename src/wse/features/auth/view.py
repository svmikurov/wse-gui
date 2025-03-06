"""Defines the login screen view."""

import toga

from wse.features.shared.view import BaseView
from wse.utils.i18n import _


class LoginView(BaseView):
    """Represents the login screen."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)

        self.heading = toga.Label(_('Login'))

        # DOM
        self.add(
            self.heading,
        )
