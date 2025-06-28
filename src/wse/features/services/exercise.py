"""Defines exercise service."""

import logging

from injector import inject

from ..base.mixins import AddObserverMixin
from ..interfaces import ISubject

logger = logging.getLogger(__name__)


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

    def update_answer(self, value: str) -> None:
        """Update user input answer."""
        self._user_answer = value
        self._subject.notify('answer_updated', value=value)
