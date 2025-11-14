"""Abstract base classes for Foreign discipline domain."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.feature.observer.mixins import ObserverManagerGen

# TODO: Refactor 'ExerciseAccessorT' to Enum?
ExerciseAccessorT = Literal['definition', 'explanation', 'timeout']
UIStateNotifyT = Literal['exercise_updated', 'timeout_updated']


class PresentationObserverABC(ABC):
    """ABC for Presentation exercise observer."""

    # TODO: Add check each 'ExerciseAccessorT' type added to ABC?

    @abstractmethod
    def exercise_updated(
        self,
        accessor: ExerciseAccessorT,
        value: str,
    ) -> None:
        """Notify that exercise updated."""


class TimeoutObserverABC(ABC):
    """ABC for timeout observer."""

    @abstractmethod
    def timeout_updated(
        self,
        accessor: ExerciseAccessorT,
        max: float,
        value: float,
    ) -> None:
        """Notify that progress updated."""


class ExerciseUserActionsABC(ABC):
    """ABC for Exercise user action."""

    @abstractmethod
    def pause(self) -> None:
        """Handle 'pause' case user action of exercise."""

    @abstractmethod
    def unpause(self) -> None:
        """Handle 'unpause' case user action of exercise."""

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
    ObserverManagerGen[PresentationObserverABC],
    ExerciseUserActionsABC,
    ABC,
):
    """ABC for Words study Use Case."""

    @abstractmethod
    def start(self) -> None:
        """Start exercise."""

    @abstractmethod
    def stop(self) -> None:
        """Stop exercise."""
