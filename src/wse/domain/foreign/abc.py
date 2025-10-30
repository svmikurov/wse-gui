"""Abstract base classes for Foreign discipline domain."""

from abc import ABC, abstractmethod
from typing import Literal

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


class ExerciseUserActionsABC(ABC):
    """ABC for Exercise user action."""

    @abstractmethod
    def pause(self) -> None:
        """Handle 'pause' case user action of exercise."""

    @abstractmethod
    def next(self) -> None:
        """Handle 'next' case user action of exercise."""

    @abstractmethod
    def known(self) -> None:
        """Handle 'known' case user action of exercise."""

    @abstractmethod
    def unknown(self) -> None:
        """Handle 'unknown' case user action of exercise."""


class WordStudyUseCaseABC(
    ObserverManagerGen[ExerciseNotifyABC],
    ExerciseUserActionsABC,
    ABC,
):
    """ABC for Words study Use Case."""

    @abstractmethod
    def start(self) -> None:
        """Start exercise."""
