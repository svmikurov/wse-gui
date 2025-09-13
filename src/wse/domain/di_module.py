"""Domain layer DI module."""

from typing import no_type_check

from injector import Binder, Module

from .abc import (
    UserObserverRegistryUseCaseABC,
)
from .protocol import (
    CheckCalculationUseCaseProto,
    UpdateQuestionUseCaseProto,
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
        # Mathematical discipline
        binder.bind(UpdateQuestionUseCaseProto, to=UpdateQuestionUseCase)
        binder.bind(CheckCalculationUseCaseProto, to=CheckCalculationUseCase)

        # User
        binder.bind(
            UserObserverRegistryUseCaseABC,
            to=UserObserverRegistryUseCase,
        )
