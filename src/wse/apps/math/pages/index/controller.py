"""Defines Main Math page controller."""

from dataclasses import dataclass
from typing import TypeVar

from injector import inject
from wse_exercises.base.enums import ExerciseEnum

from wse.apps.math.api import Calculation
from wse.apps.nav_id import NavID
from wse.core.interfaces import Navigable
from wse.feature.base.mvc import PageController
from wse.feature.interfaces.imvc import ModelProto
from wse.feature.shared.containers.top_bar import TopBarControllerMixin

from .abc import MathModelNavigateObserver
from .protocols import MathModelProto, MathViewProto

ModelT = TypeVar('ModelT', bound=ModelProto)


class _ModelObserver(
    MathModelNavigateObserver,
):
    """Mixin providing observe on Index Math page model."""

    _navigator: Navigable

    def exercise_started(self, value: Calculation) -> None:
        """Navigate to exercise page."""
        self._navigator.navigate(nav_id=NavID.SIMPLE_CALC, value=value)


class _ViewObserver:
    """Mixin providing observe on Index Math page view."""

    _model: MathModelProto

    def exercise_changed(self, value: ExerciseEnum) -> None:
        """Handle the change of exercise type."""
        self._model.change_exercise(value)

    def start_button_pressed(self) -> None:
        """Handle the start exercise button pressed."""
        self._model.start_exercise()


@inject
@dataclass
class MathController(
    TopBarControllerMixin[MathViewProto],
    PageController[MathModelProto, MathViewProto, None],
    _ModelObserver,
    _ViewObserver,
):
    """Main Math page controller."""

    _model: MathModelProto
    _view: MathViewProto

    def on_open(self, value: None = None) -> None:
        """Call methods when page opens."""
        self._model.update_page_context()
