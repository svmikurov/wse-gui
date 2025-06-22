"""Defines protocols for MVC model components interface."""

from typing import Protocol, runtime_checkable

from .icontent import IContentDependency


class IView(
    IContentDependency,
    Protocol,
):
    """Protocol for page view interface."""

    def add_observer(self, observer: object) -> None:
        """Subscribe observer an event has occurred."""


@runtime_checkable
class IController(
    IContentDependency,
    Protocol,
):
    """Protocol for page controller interface."""
