"""Assigned exercise View."""

import logging
from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.core.navigation.nav_id import NavID
from wse.ui.math.calculation.view import CalculationView

from .abc import AssignedExerciseViewModelABC

logger = logging.getLogger(__name__)


@inject
@dataclass
class AssignedCalculationView(
    CalculationView,
):
    """Assigned calculation exercise view."""

    # TODO: Fix type ignore
    _state: AssignedExerciseViewModelABC  # type: ignore[assignment]

    @override
    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self._content.test_id = NavID.ASSIGNED

    @override
    def on_open(self) -> None:
        """Call methods on screen open."""
        super().on_open()
        self._state.refresh_context()
