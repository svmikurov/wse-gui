"""Defines protocol and abc for account state inspector."""

from abc import ABC, abstractmethod
from typing import Any, Protocol

from typing_extensions import override


class IAccountStateInspector(Protocol):
    """Protocol for account state inspector interface."""

    def inspect(self, data: dict[str, Any]) -> None:
        """Inspect the response data."""


class BaseAccountStateInspector(ABC, IAccountStateInspector):
    """Base class for account state inspector."""

    @abstractmethod
    @override
    def inspect(self, data: dict[str, Any]) -> None:
        """Inspect the response data."""
