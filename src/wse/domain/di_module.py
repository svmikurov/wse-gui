"""Domain layer DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from .abc import (
    PresentationABC,
)
from .abc.assigned import (
    CheckAssignedAnswerUseCaseABC,
    GetAssignedQuestionUseCaseABC,
    GetAssignedSolutionUseCaseABC,
    SetAssignedExerciseUseCaseABC,
)
from .abc.calculation import (
    CheckCalculationAnswerUseCaseABC,
    GetCalculationQuestionUseCaseABC,
    GetCalculationSolutionUseCaseABC,
)
from .abc.user import UserObserverRegistryUseCaseABC
from .assigned import (
    CheckAssignedAnswerUseCase,
    GetAssignedQuestionUseCase,
    GetAssignedSolutionUseCase,
    SetAssignedExerciseUseCase,
)
from .foreign.abc import WordStudyUseCaseABC
from .foreign.study import WordStudyUseCase
from .glossary import (
    GetTermsUseCaseABC,
    SubscribeTermsUseCaseABC,
    TermPresentationUseCaseABC,
)
from .glossary.observer import SubscribeTermsUseCase
from .glossary.presentation import TermPresentationUseCase
from .glossary.terms import GetTermsUseCase
from .math_task import (
    CheckCalculationAnswerUseCase,
    GetCalculationQuestionUseCase,
    GetCalculationSolutionUseCase,
)
from .presentation import Presentation
from .text import TextHyphenationABC
from .text.hyphenation import TextHyphenation
from .user import UserObserverRegistryUseCase


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

        # Presentation domain
        binder.bind(PresentationABC, to=Presentation)

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

        # Glossary
        binder.bind(SubscribeTermsUseCaseABC, to=SubscribeTermsUseCase)
        binder.bind(GetTermsUseCaseABC, to=GetTermsUseCase)
        binder.bind(TermPresentationUseCaseABC, to=TermPresentationUseCase)

        # Foreign
        binder.bind(WordStudyUseCaseABC, to=WordStudyUseCase)

        # Text
        binder.bind(TextHyphenationABC, to=TextHyphenation)
