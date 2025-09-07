"""Task Use Cases."""

from typing_extensions import override

from .abc import (
    BaseCheckCalculationUseCase,
    BaseGetQuestionUseCase,
)


class GetQuestionUseCase(BaseGetQuestionUseCase):
    """Fetch calculation exercise task question Use Case."""

    @override
    def fetch(self) -> None:
        """Get task question."""
        self._repository.fetch_task()


class CheckCalculationUseCase(BaseCheckCalculationUseCase):
    """Check calculation exercise user task answer Use Case."""

    @override
    def check(self, answer: str) -> None:
        """Check user answer."""
        self._repository.check_answer(answer)
