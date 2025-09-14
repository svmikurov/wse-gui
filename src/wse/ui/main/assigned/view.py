"""Assigned exercise View."""

from dataclasses import dataclass

from injector import inject

from wse.ui.math.calculation.view import CalculationView

from .abc import AssignedExerciseViewModelABC


@inject
@dataclass
class AssignedCalculationView(CalculationView):
    """Assigned calculation exercise view."""

    # TODO: Fix type ignore
    _state: AssignedExerciseViewModelABC  # type: ignore[assignment]
