"""Defines protocol for widget interfaces."""

from typing import Any, Iterable, Protocol

from toga.sources import Source

from wse.core.navigation.nav_id import NavID

from ..interfaces.istyle import StyleMixinProto


class NavigableButton(
    StyleMixinProto,
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


class SelectionProto(Protocol):
    """Protocol for Selection widget."""

    @property
    def items(self) -> Source:
        """The items to display in the selection."""

    @items.setter
    def items(self, items: Source | Iterable[Any] | None) -> None: ...
