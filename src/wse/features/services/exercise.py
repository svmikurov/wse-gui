"""Defines exercise service."""

import logging
from dataclasses import dataclass

from injector import inject

from ..base.mixins import AddObserverMixin
from ..interfaces import ISubject
from .interfaces import ITask

logger = logging.getLogger(__name__)


@dataclass
class Task:
    """Exercise task."""

    question: str
    answer: str


@inject
class ExerciseService(
    AddObserverMixin,
):
    """Exercise service."""

    def __init__(
        self,
        subject: ISubject,
    ) -> None:
        """Construct the exercise."""
        self._subject = subject
        self._user_answer: str | None = None

    @staticmethod
    def get_task() -> ITask:
        """Get task."""
        return Task(
            question='1 + 3',
            answer='4',
        )
