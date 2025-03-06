"""Defines the main screen view."""

from wse.features.shared.ui.heading import Heading
from wse.features.shared.view import BaseView


class HomeView(BaseView):
    """Represents the home screen."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)

        self.heading = Heading('Home')

        # DOM
        self.add(
            self.heading,
        )
