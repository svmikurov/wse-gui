"""Abstract base classes for Foreign words study screen."""

from abc import ABC
from dataclasses import dataclass
from typing import Literal

from wse.domain.foreign import ExerciseNotifyABC
from wse.feature.observer import ChangeObserverABC
from wse.feature.observer.generic import (
    HandleObserverABC,
    ObserverManagerGenABC,
)
from wse.ui.base.navigate import NavigateABC, OnCloseABC, OnOpenABC
from wse.ui.base.view import ViewABC
from wse.ui.containers.control import Action

PresenterNotifyT = Literal['change']


@dataclass
class WordPresentationViewModelABC(
    OnCloseABC,
    OnOpenABC,
    NavigateABC,
    ObserverManagerGenABC[
        ChangeObserverABC[PresenterNotifyT] | HandleObserverABC[Action]
    ],
    HandleObserverABC[Action],
    ExerciseNotifyABC,
    ABC,
):
    """ABC for Foreign words study ViewModel."""


@dataclass
class StudyForeignViewABC(
    HandleObserverABC[Action],
    OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Foreign words study View."""
