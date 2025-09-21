"""Abstract base classes for Glossary discipline sources."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.feature.api.glossary.schema import (
    TermPresentationSchema,
    TermSchema,
)

from ..base import AccessorSourceABC

_NotifyT = Literal['change']
_AccessorT = Literal['case', 'text']


class TermPresentationListenrABC(ABC):
    """ABC for Term Presentation listener."""

    @abstractmethod
    def change(self, accessor: _AccessorT, value: str) -> None:
        """Change value by accessor."""


class TermNetworkSourceABC(ABC):
    """ABC for Term Network source."""

    @abstractmethod
    def get_terms(self) -> list[TermSchema] | None:
        """Get terms."""


class TermPresentationNetworkSourceABC(
    AccessorSourceABC[
        TermPresentationListenrABC,
        _NotifyT,
        _AccessorT,
    ],
    ABC,
):
    """ABC for Term Network source."""

    @abstractmethod
    def get_presentation(self) -> TermPresentationSchema | None:
        """Get Terms presentation."""
