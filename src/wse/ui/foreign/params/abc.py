"""Abstract base classes for Word study params screen."""

from abc import ABC, abstractmethod
from typing import Any

from wse.feature.observer.generic import ObserverManagerGenABC
from wse.ui.base.navigate import (
    CreateNavButtonABC,
    NavigateABC,
    OnCloseABC,
    OnOpenABC,
)
from wse.ui.base.view import ViewABC


class WordStudyParamsViewModelABC(
    ObserverManagerGenABC[Any],
    OnOpenABC,
    OnCloseABC,
    NavigateABC,
    ABC,
):
    """ABC for Word study params ViewModel."""

    @abstractmethod
    def start_exercise(self) -> None:
        """Start exercise."""


class WordStudyParamsViewABC(
    CreateNavButtonABC,
    OnOpenABC,
    OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Word study params View."""
