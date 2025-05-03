"""Defines an answer checkers to the task."""

from wse.interface.iexercise import IAnswer, ICheckResult


class AnswerChecker:
    """Answer checker."""

    def __init__(self, check_result: ICheckResult) -> None:
        """Construct the answer checker."""
        self._check_result = check_result

    def check(
        self,
        user_answer: IAnswer,
        correct_answer: IAnswer,
    ) -> ICheckResult:
        """Check the answer to the task."""
        self._check_result.is_correct = user_answer == correct_answer
        return self._check_result
