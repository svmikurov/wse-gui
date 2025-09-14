"""Abstract base classes for Calculation exercise UI layer."""

from abc import ABC
from typing import Literal

from wse.data.sources.task import TaskObserverABC
from wse.feature.base import ViewABC
from wse.feature.base.mixins import AddObserverGenT
from wse.feature.shared.containers import NumpadObserverABC
from wse.ui.base.abc import NavigateABC
from wse.ui.base.task import TaskViewModelFeatureABC, TaskViewModelObserverABC

_StateNotifyT = Literal[
    'question_updated',
    'answer_updated',
    'answer_incorrect',
    'solution_updated',
    'balance_updated',
    'state_reset',
]
_WidgetNotifyT = Literal['navigate']


# ViewModel


class CalculationViewModelObserverABC(
    TaskViewModelObserverABC,
    ABC,
):
    """ABC for Calculation exercise ViewModel observer."""


class CalculationViewModelABC(
    AddObserverGenT[CalculationViewModelObserverABC, _StateNotifyT],
    TaskViewModelFeatureABC,
    TaskObserverABC,
    NavigateABC,
    ABC,
):
    """ABC for Assigned exercise ViewModel."""


# View


class CalculationViewABC(
    CalculationViewModelObserverABC,
    NumpadObserverABC,
    ViewABC,
    ABC,
):
    """ABC for Calculation exercise View."""
