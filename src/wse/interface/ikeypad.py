"""Defines protocol interfaces for keypad."""

from typing import Callable, Protocol

import toga

from wse.interface.ifeatures import ISubject

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off


class IKeypad(Protocol):
    """Protocol defining the interface for keypad."""
    @property
    def content(self) -> [toga.Widget]:
        """Widgets of keypad."""

    def subscribe(self, listener: object) -> None:
        """Register an observer to receive notifications."""