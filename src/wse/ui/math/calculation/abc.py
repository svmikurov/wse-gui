"""Abstract base classes for Calculation exercise UI layer."""

from abc import ABC
from typing import Literal

from wse.data.sources.task import TaskObserverABC
from wse.feature.base.mixins import AddObserverGenT
from wse.feature.shared.containers import NumpadObserverABC
from wse.ui.base.abc.navigate import NavigateABC
from wse.ui.base.abc.utils import OnCloseABC
from wse.ui.base.abc.view import ViewABC
from wse.ui.base.task_abc import (
    TaskViewModelFeatureABC,
    TaskViewModelObserverABC,
)

_StateNotifyT = Literal[
    'question_updated',
    'answer_updated',
    'answer_incorrect',
    'solution_updated',
    'balance_updated',
    'task_reset',
]
_WidgetNotifyT = Literal['navigate']

# ViewModel


class CalculationViewModelABC(
    AddObserverGenT[TaskViewModelObserverABC, _StateNotifyT],
    TaskViewModelFeatureABC,
    TaskObserverABC,
    NavigateABC,
    OnCloseABC,
    ABC,
):
    """ABC for Assigned exercise ViewModel."""


# View


class CalculationViewABC(
    TaskViewModelObserverABC,
    NumpadObserverABC,
    ViewABC,
    OnCloseABC,
    ABC,
):
    """ABC for Calculation exercise View."""
