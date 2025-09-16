"""Domain layer DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from .abc import (
    CheckAssignedAnswerUseCaseABC,
    CheckCalculationAnswerUseCaseABC,
    GetAssignedQuestionUseCaseABC,
    GetAssignedSolutionUseCaseABC,
    GetCalculationQuestionUseCaseABC,
    GetCalculationSolutionUseCaseABC,
    SetAssignedExerciseUseCaseABC,
    UserObserverRegistryUseCaseABC,
)
from .assigned import (
    CheckAssignedAnswerUseCase,
    GetAssignedQuestionUseCase,
    GetAssignedSolutionUseCase,
    SetAssignedExerciseUseCase,
)
from .math_task import (
    CheckCalculationAnswerUseCase,
    GetCalculationQuestionUseCase,
    GetCalculationSolutionUseCase,
)
from .user import (
    UserObserverRegistryUseCase,
)


class UseCaseModule(Module):
    """Domain layer DI module for Use Cases."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # User
        binder.bind(
            UserObserverRegistryUseCaseABC,
            to=UserObserverRegistryUseCase,
        )

        # Mathematical discipline
        binder.bind(
            GetCalculationQuestionUseCaseABC,
            to=GetCalculationQuestionUseCase,
            scope=SingletonScope,
        )
        binder.bind(
            CheckCalculationAnswerUseCaseABC,
            to=CheckCalculationAnswerUseCase,
        )
        binder.bind(
            GetCalculationSolutionUseCaseABC,
            to=GetCalculationSolutionUseCase,
        )

        # Assigned exercise
        binder.bind(
            SetAssignedExerciseUseCaseABC,
            to=SetAssignedExerciseUseCase,
        )
        binder.bind(
            GetAssignedQuestionUseCaseABC,
            to=GetAssignedQuestionUseCase,
        )
        binder.bind(
            CheckAssignedAnswerUseCaseABC,
            to=CheckAssignedAnswerUseCase,
        )
        binder.bind(
            GetAssignedSolutionUseCaseABC,
            to=GetAssignedSolutionUseCase,
        )
