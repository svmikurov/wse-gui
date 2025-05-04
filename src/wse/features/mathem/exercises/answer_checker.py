"""Defines an answer checkers to the task."""

import logging

from wse.core.i18n import _
from wse.interface.iexercise import IAnswer, IResult, ITaskStorage

logger = logging.getLogger(__name__)


class Result:
    """Task answer checking result."""

    NO_COMMENTS = ''

    def __init__(self, is_correct: bool) -> None:
        """Construct the check result."""
        self._is_correct = is_correct

    @property
    def is_correct(self) -> bool:
        """Whether the user's answer matches the correct solution."""
        return self._is_correct

    @property
    def text(self) -> str:
        """Return the text representation of check result."""
        if self.is_correct:
            return self.NO_COMMENTS
        return _('Wrong')

    def __str__(self) -> str:
        """Return the string representation of check result."""
        return str(self.is_correct)


class AnswerChecker:
    """Answer checker."""

    def __init__(self) -> None:
        """Construct the answer checker."""
        self._is_correct: bool | None = None

    def check(self, user_answer: IAnswer, storage: ITaskStorage) -> None:
        """Verify user's answer against stored correct solution."""
        self._is_correct = user_answer.text == storage.answer.text

    @property
    def result(self) -> IResult:
        """The representation of user answer check."""
        return Result(self._is_correct)
