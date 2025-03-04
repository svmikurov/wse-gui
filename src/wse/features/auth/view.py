"""Authentication view."""

import toga

from wse.features.share.view import BaseView


class LoginView(BaseView):
    """Login screen view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)

        self.heading = toga.Label('Login')

        # DOM
        self.add(
            self.heading,
        )
