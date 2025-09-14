"""Exercise repository."""

import logging
from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.config.api_paths import MathAPIConfigV1
from wse.core.api import RelatedData
from wse.feature.api.math import Calculation
from wse.feature.api.math.protocol import CalculationApiProto
from wse.feature.api.math.schema import CalculationCondition, CalculationConfig
from wse.feature.shared.schemas.task import Answer, Question, Result

from ..sources import TaskSource
from ..sources.task import TaskObserverT
from .abc import CalculationTaskRepoABC
from .calculation_exercises import CalculationExerciseRepo
from .http_related import (
    RelatedDataHttpResponseRepoABC,
)

logger = logging.getLogger(__name__)


@inject
@dataclass
class CalculationTaskRepo(CalculationTaskRepoABC):
    """Protocol for calculation task repository interface."""

    _api_client: CalculationApiProto
    _api_config: MathAPIConfigV1
    _task_source: TaskSource
    _exercise_source: CalculationExerciseRepo
    _related_data_repo: RelatedDataHttpResponseRepoABC

    @override
    def fetch_task(self) -> None:
        """Fetch calculation exercise task question."""
        if response := self._api_client.request_task(self._get_exercise()):
            self._update_task(response.data)
            self._handle_related(response.related_data)

    @override
    def fetch_result(self, answer: str) -> None:
        """Fetch user answer check result."""
        if not self._task_source.uid:
            logger.error('Task identifier was not set')
            return None

        if response := self._api_client.check_answer(
            answer=Answer(uid=self._task_source.uid, answer=answer),
            exercise=self._get_exercise(),
        ):
            self._update_result(response.data)
            self._handle_related(response.related_data)

        return None

    # TODO: Fix development implementation of method
    def _get_exercise(self) -> Calculation:
        return Calculation(
            question_url_path=self._api_config.calculation.get_task,
            check_url_path=self._api_config.calculation.validate_answer,
            task_io='text',
            condition=CalculationCondition(
                exercise_name=self._exercise_source.default,
                config=CalculationConfig(
                    min_value='1',
                    max_value='9',
                ),
            ),
        )

    def _update_task(self, data: Question) -> None:
        self._task_source.update_task(data)

    def _update_result(self, data: Result) -> None:
        self._task_source.update_result(data)

    def _handle_related(self, data: RelatedData | None) -> None:
        if data is not None:
            self._related_data_repo.update_related(data)

    def add_observer(
        self,
        listener: TaskObserverT,
    ) -> None:
        """Subscribe listener to repository notifications."""
        self._task_source.add_listener(listener)

    def update_solution(self) -> None:
        """Set current solution."""
        self._task_source.update_solution()
