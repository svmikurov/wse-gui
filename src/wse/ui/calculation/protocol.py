"""Defines protocols for Simple Math Calculation page components."""

from typing import Protocol

from wse.apps.nav_id import NavID
from wse.feature.interfaces.icontent import GetContentProto


class CalculationModelViewProto(Protocol):
    """Protocol for Calculation exercise page ModelView interface."""

    def submit_answer(self) -> None:
        """Submit user answer."""

    def get_task(self) -> None:
        """Get next task."""

    def navigate(self, nav_id: NavID) -> None:
        """Notify to navigate."""


class CalculationViewProto(
    GetContentProto,
    Protocol,
):
    """Protocol for Calculation view."""
