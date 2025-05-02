"""Defines Multiplication page controller."""

from __future__ import annotations

import dataclasses
import logging
from typing import TYPE_CHECKING

from wse.features.base.mvc import ContextController
from wse.features.shared.action_id import ActionID
from wse.features.shared.ui_names import UIName
from wse.interface.iobserver import IStateSubject

if TYPE_CHECKING:
    from wse.features.mathem import MultiplicationModel, MultiplicationView

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class MultiplicationController(ContextController):
    """Multiplication page controller."""

    model: MultiplicationModel
    view: MultiplicationView

    def __post_init__(self) -> None:
        """Post init."""
        # Subscribe to model notifications
        self.model.subject.add_listener(self)
        # Subscribe to view notifications
        self.view.button_handler.subject.add_listener(self)
        self.view.keypad.subscribe(listener=self)

    # Listening to model notification

    @property
    def named_ui(self) -> dict[UIName, IStateSubject]:
        """Get a UI by name to manage its state."""
        return {
            UIName.QUESTION_DISPLAY: self.view.display_question,
            UIName.ANSWER_DISPLAY: self.view.display_answer,
        }

    def change_ui_value(self, ui_name: UIName, value: str) -> None:
        """Change the text value for UI."""
        ui = self.named_ui.get(ui_name)
        ui.change(value)

    def clean_ui_value(self, ui_name: UIName) -> None:
        """Clear the text value in UI."""
        ui = self.named_ui.get(ui_name)
        ui.clean()

    # Listening to view notification

    def handel_keypad_press(self, value: str) -> None:
        """Handle keypad button press and notify Subject."""
        self.model.display_answer.change(value)

    def handle_button(self, value: str) -> None:
        """Handle button press and notify Subject."""
        match value:
            case ActionID.CHECK_ANSWER:
                result = self.model.check_answer()
                logger.debug(f'Checking result: {result}')
