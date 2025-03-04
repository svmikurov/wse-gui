"""Main model."""

from wse.features.share.ui.heading import Heading
from wse.features.share.view import BaseView


class HomeView(BaseView):
    """Home screen view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)

        self.heading = Heading('Home')

        # DOM
        self.add(
            self.heading,
        )
