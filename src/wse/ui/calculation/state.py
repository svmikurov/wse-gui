"""Calculation exercise ModelView."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.core.interfaces import Navigable
from wse.domain import (
    CheckCalculationUseCaseProto,
    GetQuestionUseCaseProto,
)

from .abc import BaseCalculationModelView


@inject
@dataclass
class CalculationModelView(
    BaseCalculationModelView,
):
    """Calculation exercise ModelView."""

    _question_case: GetQuestionUseCaseProto
    _result_case: CheckCalculationUseCaseProto
    _navigator: Navigable

    @override
    def submit_answer(self) -> None:
        """Submit user answer."""

    @override
    def get_task(self) -> None:
        """Get next task."""

    @override
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event, callback."""
        self._navigator.navigate(nav_id=nav_id)
