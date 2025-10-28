"""Abstract base classes for Foreign words study screen."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from wse.feature.observer import UpdateObserverABC
from wse.feature.observer.generic import ObserverManagerGenABC
from wse.ui.base.navigate import NavigateABC, OnCloseABC
from wse.ui.base.view import ViewABC


@dataclass
class StudyForeignViewModelABC(
    OnCloseABC,
    NavigateABC,
    ObserverManagerGenABC[UpdateObserverABC[Any]],
    ABC,
):
    """ABC for Foreign words study ViewModel."""

    @abstractmethod
    def on_open(self) -> None:
        """Call methods on screen open."""


@dataclass
class StudyForeignViewABC(
    OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Foreign words study View."""
