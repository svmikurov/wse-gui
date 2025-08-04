"""Defines the protocols for services interface."""

from typing import Any, Protocol

from wse.apps.math.pages.simple_calc.dto import CalcResultDTO, CalcTaskDTO


class ICalcService(Protocol):
    """Protocols for Exercise Service interface."""

    def get_task(self, data: dict[str, Any]) -> CalcTaskDTO:
        """Get task."""

    def check_answer(self, user_answer: str) -> CalcResultDTO:
        """Check the user answer."""
