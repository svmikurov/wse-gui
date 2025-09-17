"""Abstract Base Classes for task."""

from abc import ABC, abstractmethod


class GetQuestionUseCaseABC(ABC):
    """ABC for get exercise task question Use Case."""

    @abstractmethod
    def update(self) -> None:
        """Fetch task question."""


class CheckAnswerUseCaseABC(ABC):
    """ABC for check exercise user answer Use Case."""

    @abstractmethod
    def check(self, answer: str) -> None:
        """Check user answer."""


class GetSolutionUseCaseABC(ABC):
    """ABC for get current solution Use Case."""

    @abstractmethod
    def update_solution(self) -> None:
        """Set current solution to Data layer."""
