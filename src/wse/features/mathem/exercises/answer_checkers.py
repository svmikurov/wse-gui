"""Defines an answer checkers to the task."""


class StrictAnswerChecker:
    """Strict answer match check."""

    def check(self, user_answer: str, correct_answer: str) -> bool:
        """Check the answer to the task."""
        return user_answer.strip() == correct_answer.strip()
