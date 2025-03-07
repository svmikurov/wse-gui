"""Defines the main screen view."""

from wse.features.shared.ui.box import ColumnFlexBox
from wse.features.shared.ui.heading import Heading
from wse.utils.i18n import _


class HomeView(ColumnFlexBox):
    """Represents the home screen."""

    def __init__(self) -> None:
        """Construct the view."""
        super().__init__()

        self.heading = Heading(_('Home'))

        # DOM
        self.add(
            self.heading,
        )
