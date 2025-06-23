"""Defines protocol for widget interfaces."""

from typing import Protocol, TypeVar

from wse.features.subapps.nav_id import NavID

StyleT = TypeVar('StyleT')


class INavButton(Protocol[StyleT]):
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
    def style(self) -> StyleT:
        """The button's style."""

    @style.setter
    def style(self, style: StyleT) -> None: ...
