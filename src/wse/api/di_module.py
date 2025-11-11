"""API requests DI module."""

from typing import no_type_check

from injector import Binder, Module
from typing_extensions import override

from .foreign import (
    WordParamsApiABC,
    WordStudyPresentationApiABC,
    WordStudyProgressApiABC,
)
from .foreign.params import WordParamsApi
from .foreign.progress import WordStudyProgressApi
from .foreign.study import WordStudyPresentationApi
from .glossary.abc import TermApiABC
from .glossary.term import TermApi
from .main.abc import AssignationsApiABC, AssignedApiABC
from .main.assignations import AssignationsApi
from .main.assigned import AssignedApiClient
from .math.abc import CalculationApiABC
from .math.calculation import CalculationApiClient


class ApiModule(Module):
    """API requests DI module."""

    @no_type_check
    @override
    def configure(self, binder: Binder) -> None:
        """Configure dependencies."""
        # Assigned
        binder.bind(AssignedApiABC, to=AssignedApiClient)
        binder.bind(AssignationsApiABC, to=AssignationsApi)

        # Calculation
        binder.bind(CalculationApiABC, to=CalculationApiClient)

        # Glossary
        binder.bind(TermApiABC, to=TermApi)

        # Foreign
        binder.bind(WordStudyPresentationApiABC, to=WordStudyPresentationApi)
        binder.bind(WordParamsApiABC, to=WordParamsApi)
        binder.bind(WordStudyProgressApiABC, to=WordStudyProgressApi)
