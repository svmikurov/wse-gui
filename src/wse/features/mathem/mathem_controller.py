"""Defines Mathematical page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from wse.core.navigation.navigation_id import NavID
from wse.features.base.mvc import ContextController

if TYPE_CHECKING:
    from wse.features.mathem import MathematicalModel, MathematicalView

logger = logging.getLogger(__name__)


@dataclass
class MathematicalController(ContextController):
    """Mathematical page controller."""

    model: MathematicalModel
    view: MathematicalView

    # Listening to the view
    def handle_button_press(self, nav_id: NavID) -> None:
        """Handel button press."""
        match nav_id:
            case NavID.MULTIPLICATION:
                self.navigate(NavID.MULTIPLICATION)

    # Listening to the model
    @staticmethod
    def display_task(value: str) -> None:
        """Display a task."""
        logger.debug(f'Displaying a task: {value}')
