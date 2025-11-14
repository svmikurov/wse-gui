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


class WordPresentationViewModelObserverABC(
    ChangeObserverABC[domain.ExerciseAccessorT],
    domain.TimeoutObserverABC,
    ABC,
):
    """ABC for Word presentation ViewModel observer."""

    @abstractmethod
    def pause_state_updated(self, value: bool) -> None:
        """Update pause state."""


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
    """ABC for Foreign words study ViewModel."""


@dataclass
class StudyForeignViewABC(
    WordPresentationViewModelObserverABC,
    ActionHandler,
    navigate.OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Foreign words study View."""
