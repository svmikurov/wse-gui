"""Abstract base class for Calculation exercise UI."""

from abc import ABC, abstractmethod

from typing_extensions import override

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
