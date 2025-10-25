"""Abstract base classes for Glossary discipline sources."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.feature.api.glossary.schemas import (
    TermPresentationSchema,
    TermSchema,
)
from wse.feature.observer.generic import UpdateObserverABC

from ..base import AccessorSourceABC

PresentationNotifyT = Literal['change']
PresentationAccessorT = Literal['case', 'text']


class TermPresentationListenerABC(
    UpdateObserverABC[PresentationAccessorT],
    ABC,
):
    """ABC for Term Presentation listener."""

    @abstractmethod
    def update(self, accessor: PresentationAccessorT, value: str) -> None:
        """Change value by accessor."""


class TermNetworkSourceABC(ABC):
    """ABC for Term Network source."""

    @abstractmethod
    def get_terms(self) -> list[TermSchema] | None:
        """Get terms."""


class TermPresentationNetworkSourceABC(
    AccessorSourceABC[
        TermPresentationListenerABC,
        PresentationNotifyT,
        PresentationAccessorT,
    ],
    ABC,
):
    """ABC for Term Network source."""

    @abstractmethod
    def get_presentation(self) -> TermPresentationSchema | None:
        """Get Terms presentation."""
