"""Domain layer DI module."""

from typing import no_type_check

from injector import Binder, Module

from . import (
    CheckCalculationUseCaseProto,
    UpdateQuestionUseCaseProto,
)
from .task import (
    CheckCalculationUseCase,
    UpdateQuestionUseCase,
)


class UseCaseModule(Module):
    """Domain layer DI module for Use Cases."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(UpdateQuestionUseCaseProto, to=UpdateQuestionUseCase)
        binder.bind(CheckCalculationUseCaseProto, to=CheckCalculationUseCase)
