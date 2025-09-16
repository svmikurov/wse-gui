"""API requests DI module."""

from typing import no_type_check

from injector import Binder, Module
from typing_extensions import override

from .glossary.abc import TermApiABC
from .glossary.term import TermApi
from .main.abc import AssignationsApiABC, AssignedApiClientABC
from .main.assignations import AssignationsApi
from .main.assigned import AssignedApiClient
from .math.calculation import CalculationApiClient
from .math.protocol import CalculationApiProto


class ApiModule(Module):
    """API requests DI module."""

    @no_type_check
    @override
    def configure(self, binder: Binder) -> None:
        """Configure dependencies."""
        # Assigned
        binder.bind(AssignedApiClientABC, to=AssignedApiClient)
        binder.bind(AssignationsApiABC, to=AssignationsApi)

        # Calculation
        binder.bind(CalculationApiProto, to=CalculationApiClient)

        # Glossary
        binder.bind(TermApiABC, to=TermApi)
