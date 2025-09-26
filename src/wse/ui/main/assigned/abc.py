"""Abstract base classes for Assigned exercise UI layer."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.data.sources.assigned import AssignedSourceObserverABC
from wse.data.sources.task import TaskObserverABC
from wse.data.sources.user import UserObserverABC
from wse.feature.observer.mixins import SubjectGen
from wse.ui.base.navigate import NavigateABC, OnCloseABC
from wse.ui.base.task.abc import (
    TaskViewModelFeatureABC,
    TaskViewModelObserverABC,
)
from wse.ui.math.calculation.view import CalculationView

# State

_StateNotifyT = Literal[
    'question_updated',
    'answer_updated',
    'answer_incorrect',
    'solution_updated',
    'balance_updated',
    'task_reset',
]
_WidgetNotifyT = Literal['navigate']


class AssignedExerciseViewModelABC(
    SubjectGen[TaskViewModelObserverABC, _StateNotifyT],
    AssignedSourceObserverABC,
    TaskViewModelFeatureABC,
    TaskObserverABC,
    UserObserverABC,
    NavigateABC,
    OnCloseABC,
    ABC,
):
    """ABC for Assigned exercise ViewModel."""

    @abstractmethod
    def refresh_context(self) -> None:
        """Refresh context."""


# View


class AssignedExerciseViewABC(
    CalculationView,
    OnCloseABC,
    ABC,
):
    """ABC for Assigned exercise View."""
