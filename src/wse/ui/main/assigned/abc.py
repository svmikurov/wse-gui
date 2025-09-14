"""Abstract base classes for Assigned exercise UI layer."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.data.sources.assigned import AssignedSourceObserverABC
from wse.data.sources.task import TaskObserverABC
from wse.data.sources.user import UserObserverABC
from wse.feature.base.mixins import (
    NavigateMixin,
)
from wse.ui.base.mixin import BalanceUpdatedMixin
from wse.ui.base.task import TaskViewModelFeatureABC
from wse.ui.math.calculation.view import CalculationView

# State

_StateNotifyT = Literal[
    'question_updated',
    'answer_updated',
    'answer_incorrect',
    'solution_updated',
    'balance_updated',
    'state_reset',
]
_WidgetNotifyT = Literal['navigate']


class AssignedExerciseViewModelABC(
    NavigateMixin,
    BalanceUpdatedMixin,
    AssignedSourceObserverABC,
    TaskViewModelFeatureABC,
    TaskObserverABC,
    UserObserverABC,
    ABC,
):
    """ABC for Assigned exercise ViewModel."""

    @abstractmethod
    def refresh_context(self) -> None:
        """Refresh context."""


# View


class AssignedExerciseViewABC(
    CalculationView,
):
    """ABC for Assigned exercise View."""
