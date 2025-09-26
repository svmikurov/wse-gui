"""Defines protocol for widget interfaces."""

from abc import ABC, abstractmethod
from typing import Any, Iterable, Protocol

import toga
from toga.sources import Source

from wse.core.navigation.nav_id import NavID
from wse.ui.base.container.abc_style import StyledABC


class NavigableButton(
    toga.Widget,
    StyledABC,
    ABC,
):
    """Protocol for navigate button interface."""

    @property
    @abstractmethod
    def nav_id(self) -> NavID:
        """Get navigation ID."""

    @property
    @abstractmethod
    def text(self) -> str:
        """The text displayed on the button."""

    @text.setter
    @abstractmethod
    def text(self, value: str | None) -> None: ...


class SelectionProto(Protocol):
    """Protocol for Selection widget."""

    @property
    def items(self) -> Source:
        """The items to display in the selection."""

    @items.setter
    def items(self, items: Source | Iterable[Any] | None) -> None: ...
