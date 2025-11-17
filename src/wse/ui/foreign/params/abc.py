"""Abstract base classes for Word study params screen."""

from abc import ABC, abstractmethod
from typing import Any

from wse.feature.observer.generic import ObserverManagerGenABC
from wse.ui.base import navigate
from wse.ui.base.view import ViewABC
from wse.ui.containers.params import ParamsAccessorEnum


class WordStudyParamsViewModelABC(
    ObserverManagerGenABC[Any],
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
    def update_widget_state(
        self,
        accessor: ParamsAccessorEnum,
        value: object,
    ) -> None:
        """Update widget context."""


class WordStudyParamsViewABC(
    navigate.CreateNavButtonABC,
    navigate.OnOpenABC,
    navigate.OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Word study params View."""

    @abstractmethod
    def source_updated(
        self,
        accessor: ParamsAccessorEnum,
        value: object,
    ) -> None:
        """Update UI via UIState accessor notification."""

    @abstractmethod
    def value_updated(
        self,
        accessor: ParamsAccessorEnum,
        value: object,
    ) -> None:
        """Update UI value via UIState accessor notification."""

    @abstractmethod
    def widget_updated(
        self,
        accessor: ParamsAccessorEnum,
        value: object,
    ) -> None:
        """Update UIState via UI accessor notification."""
