"""Abstract base classes for Assigned exercise UI layer."""

from abc import ABC
from typing import Literal

from wse.data.sources.assigned import AssignedSourceObserverABC
from wse.data.sources.task import TaskObserverABC
from wse.data.sources.user import UserObserverABC
from wse.feature.base import ViewABC
from wse.feature.base.mixins import (
    AddObserverGen,
    AddObserverGenT,
    NavigateMixin,
)
from wse.feature.shared.containers import NumpadObserverABC
from wse.ui.base.mixin import BalanceUpdatedMixin
from wse.ui.base.task import TaskViewModelFeatureABC, TaskViewModelObserverABC

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
    AddObserverGenT[TaskViewModelObserverABC, _StateNotifyT],
    NavigateMixin,
    BalanceUpdatedMixin,
    AssignedSourceObserverABC,
    TaskViewModelFeatureABC,
    TaskObserverABC,
    UserObserverABC,
    ABC,
):
    """ABC for Assigned exercise ViewModel."""


# View


class AssignedExerciseViewABC(
    AddObserverGen[_WidgetNotifyT],
    NumpadObserverABC,
    TaskViewModelObserverABC,
    ViewABC,
    ABC,
):
    """ABC for Assigned exercise View."""
