"""Abstract Base Classes for Calculation exercise Use Cases."""

from abc import ABC

from injector import inject

from wse.data.repos.abc import CalculationTaskRepoABC
from wse.domain.abc.task import (
    CheckAnswerUseCaseABC,
    GetQuestionUseCaseABC,
    GetSolutionUseCaseABC,
)


class _BaseCalculationUseCase:
    """Base calculation exercise Use Case."""

    @inject
    def __init__(self, repository: CalculationTaskRepoABC) -> None:
        """Construct the repository."""
        self._repository = repository


class GetCalculationQuestionUseCaseABC(
    _BaseCalculationUseCase,
    GetQuestionUseCaseABC,
    ABC,
):
    """ABC for get Calculation exercise task question Use Case."""


class CheckCalculationAnswerUseCaseABC(
    _BaseCalculationUseCase,
    CheckAnswerUseCaseABC,
    ABC,
):
    """ABC for get Calculation exercise user answer Use Case."""


class GetCalculationSolutionUseCaseABC(
    _BaseCalculationUseCase,
    GetSolutionUseCaseABC,
    ABC,
):
    """ABC for get Calculation correct solution Use Case."""


# ABC for Assigned exercise Use Cases
