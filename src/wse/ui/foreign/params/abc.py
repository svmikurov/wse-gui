"""Abstract base classes for Word study params screen."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Literal, TypeAlias

from wse.feature.observer.generic import ObserverManagerGenABC
from wse.ui.base import navigate
from wse.ui.base.view import ViewABC

if TYPE_CHECKING:
    from wse.data.dto import foreign as dto

NotifyT: TypeAlias = Literal['values_updated', 'value_updated']


class ParametersViewModelObserverABC(ABC):
    """ABC for Word study Parameters ViewModel observe."""

    @abstractmethod
    def values_updated(
        self,
        accessor: dto.OptionAccessor,
        values: dto.Options,
    ) -> None:
        """Update Parameters container values."""

    @abstractmethod
    def value_updated(
        self,
        accessor: dto.ParameterAccessors,
        value: dto.Selected,
    ) -> None:
        """Update Parameters container value."""


class WordStudyParamsViewModelABC(
    ObserverManagerGenABC[ParametersViewModelObserverABC],
    navigate.OnOpenABC,
    navigate.OnCloseABC,
    navigate.NavigateABC,
    ABC,
):
    """ABC for Word study params ViewModel."""

    @abstractmethod
    def start_exercise(self) -> None:
        """Start exercise."""

    @abstractmethod
    def update_from_widget(
        self,
        accessor: dto.ParameterAccessors,
        value: str | dto.Selected | None,
    ) -> None:
        """Update widget context."""

    @abstractmethod
    def save_params(self) -> None:
        """Save selected params."""

    @abstractmethod
    def reset_params(self) -> None:
        """Reset selected params."""


class WordStudyParamsViewABC(
    navigate.CreateNavButtonABC,
    navigate.OnOpenABC,
    navigate.OnCloseABC,
    ViewABC,
    ParametersViewModelObserverABC,
    ABC,
):
    """ABC for Word study params View."""

    @abstractmethod
    def widget_updated(
        self,
        accessor: dto.ParameterAccessors,
        value: str | dto.Selected | None,
    ) -> None:
        """Update UIState via UI accessor notification."""
