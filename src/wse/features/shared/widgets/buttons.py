"""Defines buttons with an additional features."""

import toga

from wse.apps.nav_id import NavID

from ...interfaces.iwidgets import INavButton


class NavButton(toga.Button, INavButton):  # type: ignore[misc]
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

    def __init__(self, *args: object, nav_id: NavID, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self._nav_id = nav_id

    @property
    def nav_id(self) -> NavID:
        """Get navigation ID."""
        return self._nav_id
