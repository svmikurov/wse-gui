"""Defines Exercise page controller."""

from __future__ import annotations

import dataclasses
import logging
from typing import TYPE_CHECKING

from wse.core.navigation.navigation_id import NavigationID
from wse.features.shared.enums.action_id import ActionID
from wse.features.shared.enums.ui_names import UIName
from wse.interface.ifeatures import IContent
from wse.interface.iobserver import IStateSubject, ISubject

if TYPE_CHECKING:
    from wse.features.mathem import ExerciseModel, MultiplicationView

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class ExerciseController:
    """Exercise page controller."""

    model: ExerciseModel
    view: MultiplicationView
    _subject: ISubject

    def __post_init__(self) -> None:
        """Post init."""
        # Subscribe to model notifications
        self.model.subject.add_listener(self)
        # Subscribe to view notifications
        self.view.button_handler.subject.add_listener(self)
        self.view.keypad.subscribe(listener=self)

    def on_open(self) -> None:
        """Call methods on page open event."""
        self.model.on_open()

    # -=== Listening for Model notifications by UI Name ===-

    @property
    def state_ui(self) -> dict[UIName, IStateSubject]:
        """Get a UI by name to manage its state."""
        return {
            UIName.QUESTION_DISPLAY: self.view.display_question,
            UIName.ANSWER_DISPLAY: self.view.display_answer,
        }

    def change_ui_value(self, ui_name: UIName, value: str) -> None:
        """Change the text value for UI."""
        ui = self.state_ui.get(ui_name)
        ui.change(value)

    def clean_ui_value(self, ui_name: UIName) -> None:
        """Clear the text value in UI."""
        ui = self.state_ui.get(ui_name)
        ui.clean()

    # -=== Listening to view notification ===-

    def handel_keypad_press(self, value: str) -> None:
        """Handle keypad button press and notify Subject."""
        self.model.display_answer.change(value)

    def handle_button(self, value: str) -> None:
        """Handle button press and notify Subject."""
        match value:
            case ActionID.CHECK_ANSWER:
                self.model.handel_answer()

    def navigate(self, nav_id: NavigationID) -> None:
        """Navigate to page, the button event listener."""
        self._subject.notify('navigate', nav_id=nav_id)

    # -=== Utility methods ===-

    @property
    def subject(self) -> ISubject:
        """Subject of observer pattern (read-only)."""
        return self._subject

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self.view.content
