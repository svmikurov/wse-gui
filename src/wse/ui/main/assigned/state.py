"""Assigned exercise UI state."""

from dataclasses import dataclass
from typing import Literal, Union

from injector import inject

from wse.core.interfaces import Navigable
from wse.domain.abc import (
    CheckAssignedAnswerUseCaseABC,
    GetAssignedQuestionUseCaseABC,
    GetAssignedSolutionUseCaseABC,
    UserObserverRegistryUseCaseABC,
)
from wse.domain.assigned import AssignedObserverRegistryUseCase
from wse.feature.base.audit import AuditMixin

from ...base.mixin import BalanceUpdatedMixin, NavigateMixin
from ...base.task_state import TaskNotifyT, TaskState, TaskViewModelMixin
from .abc import AssignedExerciseViewModelABC

NotifyT = Literal['balance_updated']


@dataclass(frozen=True)
class AssignedExerciseUIState(TaskState):
    """Assigned exercise UI state data."""

    balance: str | None = None


@inject
@dataclass
class AssignedExerciseViewModel(
    BalanceUpdatedMixin,
    NavigateMixin,
    TaskViewModelMixin,
    AssignedExerciseViewModelABC,
    AuditMixin,
):
    """Assigned exercise ViewModel."""

    _navigator: Navigable

    _question_case: GetAssignedQuestionUseCaseABC
    _result_case: CheckAssignedAnswerUseCaseABC
    _solution_case: GetAssignedSolutionUseCaseABC

    _user_observer_case: UserObserverRegistryUseCaseABC
    _task_observer_case: AssignedObserverRegistryUseCase

    def __post_init__(self) -> None:
        """Construct the state."""
        self._data: AssignedExerciseUIState = AssignedExerciseUIState()
        self._task_observer_case.add_observer(self)
        self._user_observer_case.add_observer(self)

    def refresh_context(self) -> None:
        """Refresh context."""
        self._notify('balance_updated', balance=self._data.balance)

    def _notify(
        self,
        notification: Union[NotifyT | TaskNotifyT],
        **kwargs: object,
    ) -> None:
        self._subject.notify(notification, **kwargs)

    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._user_observer_case.remove_observer(self)
        self._task_observer_case.remove_observer(self)
