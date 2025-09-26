"""Abstract base classes for Calculation exercise UI layer."""

from abc import ABC
from typing import Literal

from wse.data.sources.task import TaskObserverABC
from wse.feature.observer.mixins import SubjectGen
from wse.ui.base.navigate import NavigateABC, OnCloseABC
from wse.ui.base.task.abc import (
    TaskViewModelFeatureABC,
    TaskViewModelObserverABC,
)
from wse.ui.base.view.abc import ViewABC
from wse.ui.containers.numpad import NumPadObserverABC

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
    SubjectGen[TaskViewModelObserverABC, _StateNotifyT],
    TaskViewModelFeatureABC,
    TaskObserverABC,
    NavigateABC,
    OnCloseABC,
    ABC,
):
    """ABC for Assigned exercise ViewModel."""


# View


class CalculationViewABC(
    NumPadObserverABC,
    TaskViewModelObserverABC,
    ViewABC,
    OnCloseABC,
    ABC,
):
    """ABC for Calculation exercise View."""
