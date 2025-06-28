"""Defines protocol for widget interfaces."""

from typing import Protocol

from ..interfaces.istyle import IStyleMixin
from ..subapps.nav_id import NavID


class INavButton(
    IStyleMixin,
    Protocol,
):
    """Protocol for navigate button interface."""

    @property
    def nav_id(self) -> NavID:
        """Get navigation ID."""

    @property
    def text(self) -> str:
        """The text displayed on the button."""

    @text.setter
    def text(self, value: str | None) -> None: ...
