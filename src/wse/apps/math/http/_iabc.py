"""Defines protocols and abc for http interfaces."""

from abc import ABC, abstractmethod
from typing import Any, Protocol

from typing_extensions import override


class IMathAPI(Protocol):
    """Protocol for mathematical app API interface."""

    def get_index_context(self) -> dict[str, Any]:
        """Get context for index page context."""


class MathAPIABC(ABC, IMathAPI):
    """ABC for math app api services."""

    @abstractmethod
    @override
    def get_index_context(self) -> dict[str, Any]:
        """Get context for index page context."""
