"""Defines application styled divider."""

import toga
from toga.style import Pack


class Divider(toga.Divider):
    """General divider for application pages."""

    def __init__(self) -> None:
        """Construct the divider."""
        style = Pack(
            height=1,
            background_color='white',
            margin_top=5,
            margin_left=30,
            margin_bottom=5,
            margin_right=30,
        )
        super().__init__(style=style)
