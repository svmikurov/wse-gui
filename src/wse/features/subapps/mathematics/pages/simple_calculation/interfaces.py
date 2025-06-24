"""Defines protocols for Simple Math Calculation page components."""

from typing import Protocol

from wse.config.layout import TextExerciseStyleConfig, TextExerciseThemeConfig
from wse.features.interfaces import IController, IView
from wse.features.interfaces.icontent import IGetContent


class ISimpleCalcView(IView, Protocol):
    """The view of Simple Math calculation page."""


class ISimpleCalcController(IController, Protocol):
    """The controller of Simple Math calculation page."""


class ISimpleMathCalcContainer(
    IGetContent,
    Protocol,
):
    """Protocol fot Simple Math calculation container interface."""

    def localize_ui(self) -> None:
        """Localize the UI text."""

    def update_style(
        self, config: TextExerciseStyleConfig | TextExerciseThemeConfig
    ) -> None:
        """Update widgets style."""
