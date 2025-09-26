"""Defines buttons with an additional features."""

import toga

from wse.core.navigation.nav_id import NavID
from wse.ui.base.iwidgets import NavigableButton


class NavButton(toga.Button, NavigableButton):
    """Navigation button.

    Added `nav_id` attribute to implement navigation.

    For example:
        ...
        self._btn_home = NavButton(
            text="To home page",
            nav_id=NavID.HOME,
            ...
        )

    """

    # TODO: Fix type ignore
    def __init__(self, *args: object, nav_id: NavID, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)  # type: ignore[arg-type]
        self._nav_id = nav_id

    @property
    def nav_id(self) -> NavID:
        """Get navigation ID."""
        return self._nav_id
