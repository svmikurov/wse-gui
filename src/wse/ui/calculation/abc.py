"""Abstract base class for Calculation exercise UI."""

from abc import ABC, abstractmethod

from typing_extensions import override

from ...apps.nav_id import NavID
from . import CalculationModelViewProto


class BaseCalculationModelView(
    ABC,
    CalculationModelViewProto,
):
    """Abstract base class for Calculation exercise ModelView."""

    @abstractmethod
    @override
    def submit_answer(self) -> None:
        """Submit user answer."""

    @abstractmethod
    @override
    def get_task(self) -> None:
        """Get next task."""

    @abstractmethod
    @override
    def navigate(self, nav_id: NavID) -> None:
        """Notify to navigate."""
