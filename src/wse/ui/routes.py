"""Screen rooters."""

from typing import no_type_check

from wse.core.navigation.nav_id import NavID
from wse.feature.interfaces.icontent import GetContentProto

from .glossary.index import IndexGlossaryViewABC
from .glossary.terms import TermsViewABC
from .main.account.abc import AuthViewABC
from .main.assignations.abc import AssignationsViewABC
from .main.assigned.abc import AssignedExerciseViewABC
from .main.home.abc import HomeViewABC
from .math.calculation.abc import CalculationViewABC
from .math.index.abc import MathIndexModelViewABC


class UIRoutes:
    """Screen routes DI module."""

    @property
    @no_type_check
    def routes(self) -> dict[NavID, GetContentProto]:
        """Get view."""
        return {
            NavID.HOME: HomeViewABC,
            # Account
            NavID.LOGIN: AuthViewABC,
            # Assigned exercises
            NavID.ASSIGNED: AssignationsViewABC,
            NavID.EXERCISE: AssignedExerciseViewABC,
            # Mathematical discipline
            NavID.MATH: MathIndexModelViewABC,
            NavID.CALCULATION: CalculationViewABC,
            # Glossary discipline
            NavID.GLOSSARY: IndexGlossaryViewABC,
            NavID.TERMS: TermsViewABC,
        }
