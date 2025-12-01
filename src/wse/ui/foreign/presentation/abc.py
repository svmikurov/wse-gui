"""Abstract base classes for Foreign words study screen."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal, TypeAlias, Union

from wse.domain import foreign as domain
from wse.feature.observer import ChangeObserverABC, generic
from wse.ui.base import navigate
from wse.ui.base.view import ViewABC
from wse.ui.containers.control import Action

ChangeNotifyT = Literal['change']

ChangeObserver: TypeAlias = ChangeObserverABC[ChangeNotifyT]
ActionHandler: TypeAlias = generic.HandleObserverGenABC[Action]
ObserverUnion: TypeAlias = Union[ChangeObserver, ActionHandler]


# TODO: Refactor: Combine `pause_state_updated` and
# `unknown_state_updated` methods?
class WordPresentationViewModelObserverABC(
    ChangeObserverABC[domain.ExerciseAccessorT],
    domain.TimeoutObserverABC,
    ABC,
):
    """ABC for Word presentation ViewModel observer."""

    @abstractmethod
    def pause_state_updated(self, value: bool) -> None:
        """Update pause state."""

    @abstractmethod
    def unknown_state_updated(self, value: bool) -> None:
        """Update unknown state."""


# TODO: Refactor multiply inherit below


@dataclass
class WordPresentationViewModelABC(
    domain.PresentationObserverABC,
    domain.TimeoutObserverABC,
    navigate.OnCloseABC,
    navigate.OnOpenABC,
    navigate.NavigateABC,
    generic.ObserverManagerGenABC[ObserverUnion],
    generic.HandleObserverGenABC[Action],
    ABC,
):
    """ABC for Word study Presentation ViewModel."""


@dataclass
class WordPresentationViewABC(
    WordPresentationViewModelObserverABC,
    ActionHandler,
    navigate.OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Word study Presentation View."""

    @abstractmethod
    def on_open(self) -> None:
        """Call methods on screen open."""

    @abstractmethod
    def on_close(self) -> None:
        """Call methods before close the screen."""

    @abstractmethod
    def timeout_updated(self, accessor: str, max: float, value: float) -> None:
        """Update progress bar."""
