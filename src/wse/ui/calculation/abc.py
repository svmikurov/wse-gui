"""Abstract base class for Calculation exercise UI."""

from abc import ABC, abstractmethod

import toga

from wse.apps.nav_id import NavID


class BaseCalculationModelView(ABC):
    """Abstract base class for Calculation exercise ModelView."""

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
    def updated_task(self, button: toga.Button) -> None:
        """Get next task."""

    @abstractmethod
    def navigate(self, nav_id: NavID) -> None:
        """Notify to navigate."""


class BaseCalculationViewModelObserver(ABC):
    """Protocol for task source observe protocol."""

    @abstractmethod
    def question_updated(self, value: str) -> None:
        """Handle the model event on task update."""

    @abstractmethod
    def answer_updated(self, value: str) -> None:
        """Handle the model event on answer update."""

    @abstractmethod
    def answer_incorrect(self, value: str) -> None:
        """Handle the model event on incorrect answer."""

    @abstractmethod
    def state_reset(self) -> None:
        """Handle the reset state event."""
