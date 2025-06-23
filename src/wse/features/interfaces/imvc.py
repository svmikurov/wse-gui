"""Defines protocols for MVC model components interface."""

from typing import Protocol, runtime_checkable

from .icontent import IGetContent


class IView(
    IGetContent,
    Protocol,
):
    """Protocol for page view interface."""

    def add_observer(self, observer: object) -> None:
        """Subscribe observer an event has occurred."""


@runtime_checkable
class IController(
    IGetContent,
    Protocol,
):
    """Protocol for page controller interface."""
