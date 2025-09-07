"""Exercise repository."""

import logging
from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.apps.math.api import Calculation
from wse.apps.math.api.protocol import CalculationApiProto
from wse.apps.math.api.schema import CalculationCondition, CalculationConfig
from wse.config.api_paths import MathAPIConfigV1
from wse.core.api import RelatedData
from wse.feature.shared.schemas.task import Answer, Question, Result

from ..sources import TaskData
from .abc import BaseCalculationRepository

logger = logging.getLogger(__name__)


@dataclass
@inject
class CalculationRepository(BaseCalculationRepository):
    """Protocol for exercise repository interface."""

    _api_client: CalculationApiProto
    _api_config: MathAPIConfigV1
    _task_data: TaskData

    @override
    def fetch_task(self) -> None:
        """Fetch calculation exercise task question."""
        if response := self._api_client.request_task(self._get_exercise()):
            self._update_question(response.data)
            self._handle_related(response.related_data)

    @override
    def check_answer(self, answer: str) -> None:
        """Check calculation exercise task user answer."""
        if not self._task_data.uid:
            logger.error('Task identifier was not set')
            return None

        if response := self._api_client.check_answer(
            Answer(uid=self._task_data.uid, answer=answer),
            self._get_exercise(),
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
                exercise_name='adding',
                config=CalculationConfig(
                    min_value='1',
                    max_value='9',
                ),
            ),
        )

    def _update_question(self, data: Question) -> None:
        self._task_data.uid = data.uid
        self._task_data.question = data.question

    # TODO: Implement method
    def _update_result(self, data: Result) -> None:
        raise NotImplementedError

    # TODO: Implement method
    def _handle_related(self, data: RelatedData | None) -> None:
        raise NotImplementedError
