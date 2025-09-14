"""Assigned exercise UI state."""

import logging
from dataclasses import dataclass, replace
from typing import TypedDict

from injector import inject
from typing_extensions import Unpack

from wse.core.interfaces import Navigable
from wse.domain.abc import (
    CheckAssignedAnswerUseCaseABC,
    GetAssignedQuestionUseCaseABC,
)
from wse.domain.assigned import AssignedObserverRegistryUseCase
from wse.domain.task_logic import AssignedLogicUseCase
from wse.ui.base.task_state import TaskViewModelMixin

from .abc import AssignedExerciseViewModelABC

logger = logging.getLogger(__name__)


class _DataFieldType(TypedDict, total=False):
    """Field types for Assigned exercise UI state data."""

    question: str
    answer: str
    solution: str
    balance: str


@dataclass(frozen=True)
class _ExerciseUIState:
    """Assigned exercise UI state data."""

    question: str | None = None
    answer: str | None = None
    solution: str | None = None
    balance: str | None = None


# TODO: Fix type ignore
@inject
@dataclass
class AssignedExerciseViewModel(
    TaskViewModelMixin,
    AssignedExerciseViewModelABC,
):
    """Assigned exercise ViewModel."""

    _navigator: Navigable

    _question_case: GetAssignedQuestionUseCaseABC
    _result_case: CheckAssignedAnswerUseCaseABC
    _logic_case: AssignedLogicUseCase

    _source_observer_case: AssignedObserverRegistryUseCase

    def __post_init__(self) -> None:
        """Construct the state."""
        self._create_data()
        self._source_observer_case.register_observer(self)

    def _create_data(self) -> None:
        """Create UI state data."""
        self._data = _ExerciseUIState()

    def _update_data(self, **data: Unpack[_DataFieldType]) -> None:
        """Update UI state data."""
        self._data = replace(self._data, **data)

    def _reset_data(self) -> None:
        """Reset UI state data."""
        self._create_data()
        self._notify('state_reset')
