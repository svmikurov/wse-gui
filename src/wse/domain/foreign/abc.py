"""Abstract base classes for Foreign discipline domain."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

from injector import inject

from wse.feature.observer.mixins import ObserverManagerGen

ExerciseAccessorT = Literal['definition', 'explanation']
UIStateNotifyT = Literal['exercise_updated']


class ExerciseNotifyABC(ABC):
    """ABC for exercise observer."""

    @abstractmethod
    def exercise_updated(
        self,
        accessor: ExerciseAccessorT,
        value: str,
    ) -> None:
        """Notify that exercise updated."""


@inject
@dataclass
class WordStudyUseCaseABC(
    ObserverManagerGen[ExerciseNotifyABC],
    ABC,
):
    """ABC for Words study Use Case."""

    @abstractmethod
    def start(self) -> None:
        """Start exercise."""
