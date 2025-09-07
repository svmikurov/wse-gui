"""Calculation exercise ModelView."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.domain import (
    CheckCalculationUseCaseProto,
    GetQuestionUseCaseProto,
)

from .abc import BaseCalculationModelView


@dataclass
@inject
class CalculationModelView(
    BaseCalculationModelView,
):
    """Calculation exercise ModelView."""

    _question_case: GetQuestionUseCaseProto
    _result_case: CheckCalculationUseCaseProto

    @override
    def submit_answer(self) -> None:
        """Submit user answer."""

    @override
    def get_task(self) -> None:
        """Get next task."""
