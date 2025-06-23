"""Defines protocols for MVC model components interface."""

from typing import Protocol, runtime_checkable

from .icontent import IGetContent
from .iobserver import IAddObserver


class IView(
    IGetContent,
    IAddObserver,
    Protocol,
):
    """Protocol for page view interface."""


@runtime_checkable
class IController(
    IGetContent,
    Protocol,
):
    """Protocol for page controller interface."""
