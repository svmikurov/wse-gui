"""Abstract base class for Calculation exercise UI."""

from abc import ABC, abstractmethod

import toga

from wse.apps.nav_id import NavID

# ViewModel


class CalculationViewModelABC(ABC):
    """Abstract base class for Calculation exercise ViewModel."""

    @abstractmethod
    def start_task(self) -> None:
        """Start new task."""

    @abstractmethod
    def update_answer(self, value: str) -> None:
        """Update user answer."""

    @abstractmethod
    def submit_answer(self, button: toga.Button) -> None:
        """Submit user answer."""

    @abstractmethod
    def update_task(self, button: toga.Button) -> None:
        """Get next task."""

    @abstractmethod
    def navigate(self, nav_id: NavID) -> None:
        """Notify to navigate."""


class CalculationViewModelObserverABC(ABC):
    """ABC for observe for ViewModel event."""

    @abstractmethod
    def question_updated(self, value: str) -> None:
        """Handle the model event on task update."""

    @abstractmethod
    def answer_updated(self, value: str) -> None:
        """Handle the model event on answer update."""

    @abstractmethod
    def answer_incorrect(self) -> None:
        """Handle the model event on incorrect answer."""

    @abstractmethod
    def solution_updated(self, solution: str) -> None:
        """Handle the model event on incorrect answer."""

    @abstractmethod
    def balance_updated(self, balance: str) -> None:
        """Handle the balance updated state event."""

    @abstractmethod
    def state_reset(self) -> None:
        """Handle the reset state event."""
