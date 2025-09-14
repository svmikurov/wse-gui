"""Domain layer DI module."""

from typing import no_type_check

from injector import Binder, Module

from .abc import (
    CheckAssignedAnswerUseCaseABC,
    CheckCalculationAnswerUseCaseABC,
    GetAssignedQuestionUseCaseABC,
    GetCalculationQuestionUseCaseABC,
    SetAssignedExerciseUseCaseABC,
    UserObserverRegistryUseCaseABC,
)
from .assigned import (
    CheckAssignedAnswerUseCase,
    GetAssignedQuestionUseCase,
    SetAssignedExerciseUseCase,
)
from .task import (
    CheckCalculationUseCase,
    UpdateQuestionUseCase,
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
            to=UpdateQuestionUseCase,
        )
        binder.bind(
            CheckCalculationAnswerUseCaseABC,
            to=CheckCalculationUseCase,
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
