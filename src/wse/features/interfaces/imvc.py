"""Defines protocols for MVC model components interface."""

from typing import Protocol, runtime_checkable

from .icontainers import IContainer
from .icontent import IGetContent


class IView(
    IContainer,
    Protocol,
):
    """Protocol for page view interface."""


@runtime_checkable
class IController(
    IGetContent,
    Protocol,
):
    """Protocol for page controller interface."""
