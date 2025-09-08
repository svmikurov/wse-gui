"""Task data type.

Note:
----
    Created for academic purposes to study the architecture used in
    Android applications.

"""

import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Literal

from injector import inject

from wse.apps.math.api import Calculation
from wse.apps.math.api.protocol import CalculationApiProto
from wse.apps.math.api.schema import CalculationCondition, CalculationConfig
from wse.feature.shared.schemas.task import Question

from .sources.base import DataSourceGen

_NotifyType = Literal['question_updated',]

# Exercise


# TODO: Refactor to pydantic type
@dataclass(frozen=True)
class DivisionExerciseData:
    """Exercise."""

    name: str = 'division'
    min_value = '1'
    max_value = '9'
    question_url_path: str = '/api/v1/math/exercise/calculation/'
    check_url_path: str = 'api/v1/math/exercise/calculation/validate/'
    task_io: str = 'text'


@inject
@dataclass
class ExerciseDataSource:
    """Exercise source."""

    _exercise: DivisionExerciseData

    def get(self) -> Calculation:
        """Get exercise."""
        return Calculation(
            question_url_path=self._exercise.question_url_path,
            check_url_path=self._exercise.check_url_path,
            task_io=self._exercise.task_io,
            condition=CalculationCondition(
                exercise_name=self._exercise.name,
                config=CalculationConfig(
                    min_value=self._exercise.min_value,
                    max_value=self._exercise.max_value,
                ),
            ),
        )


# Task


# TODO: Refactor to pydantic type
@dataclass(frozen=True)
class TaskData:
    """Exercise task."""

    uid: uuid.UUID | None
    question: str | None
    correct_answer: str | None = None
    user_answer: str | None = None
    completed: bool = False
    created_at: datetime = datetime.now()
    updated_at: datetime | None = None


class BaseTaskObserver(ABC):
    """Task data notifications observer."""

    @abstractmethod
    def question_updated(self, data: Question) -> None:
        """Question updated."""


@inject
@dataclass
class TaskNetworkDataSource(
    DataSourceGen[BaseTaskObserver, _NotifyType],
):
    """Exercise task network source."""

    _api: CalculationApiProto
    _exercise: ExerciseDataSource

    def __post_init__(self) -> None:
        """Construct the source."""
        self._task: TaskData | None = None

    def fetch(self) -> None:
        """Fetch task."""
        response = self._api.request_task(self._exercise.get())
        if response and response.data:
            self._create(response.data)

    def _create(self, question: Question) -> None:
        """Create task."""
        self._task = TaskData(**question.to_dict())
        self.notify('question_updated', value=self._task.question)


@inject
@dataclass
class TaskDataRepository:
    """Task repository."""

    _task_source: TaskNetworkDataSource

    def add_listener(self, listener: BaseTaskObserver) -> None:
        """Add task listener."""
        self._task_source.add_listener(listener)

    def update_question(self) -> None:
        """Update task question."""
