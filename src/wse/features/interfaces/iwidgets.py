"""Defines protocol for widget interfaces."""

from typing import Protocol

from wse.features.interfaces.istyle import IStyle
from wse.features.subapps.nav_id import NavID


class INavButton(Protocol):
    """Protocol for navigate button interface."""

    @property
    def nav_id(self) -> NavID:
        """Get navigation ID."""

    @property
    def text(self) -> str:
        """The text displayed on the button."""

    @text.setter
    def text(self, value: str | None) -> None: ...

    @property
    def style(self) -> IStyle:
        """The button's style."""

    @style.setter
    def style(self, style: IStyle) -> None: ...
