"""Defines protocols for Simple Math Calculation page components."""

from typing import Protocol

import toga

from wse.apps.nav_id import NavID
from wse.feature.interfaces.icontent import GetContentProto
from wse.feature.interfaces.iobserver import AddObserverProto


class CalculationViewModelProto(
    AddObserverProto,
    Protocol,
):
    """Protocol for Calculation exercise page ViewModel interface."""

    def start_task(self) -> None:
        """Start new task."""

    def update_answer(self, answer: str) -> None:
        """Update user answer."""

    def submit_answer(self, button: toga.Button) -> None:
        """Submit user answer, button callback."""

    def update_task(self, button: toga.Button) -> None:
        """Get next task, button callback."""

    def navigate(self, nav_id: NavID) -> None:
        """Notify to navigate."""


class CalculationViewModelObserverProto(Protocol):
    """Protocol for task source observe protocol."""

    def question_updated(self, value: str) -> None:
        """Handle the model event on task update."""

    def answer_updated(self, value: str) -> None:
        """Handle the model event on answer update."""

    def answer_incorrect(self, value: str) -> None:
        """Handle the model event on incorrect answer."""

    def state_reset(self) -> None:
        """Handle the reset state event."""


class CalculationViewProto(
    GetContentProto,
    CalculationViewModelObserverProto,
    Protocol,
):
    """Protocol for Calculation view."""
