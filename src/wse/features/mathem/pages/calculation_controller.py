"""Defines the controller for the Multiplication Exercise page."""

from dataclasses import dataclass
from typing import Iterable

from wse.core.navigation.navigation_id import NavID
from wse.features.mathem.interfaces.ipages import (
    ICalculationController,
    ICalculationModel,
    ICalculationView,
)
from wse.features.shared.enums import FieldID, TaskState
from wse.features.shared.enums.notify_id import NotifyID
from wse.interfaces.ifeatures.icontent import IContent
from wse.interfaces.iobserver import IStateSubject, ISubject
from wse.interfaces.iui.ikeypad import IKeypadModel


@dataclass
class CalculationController(ICalculationController):
    """Multiplication exercise page controller."""

    model: ICalculationModel
    keypad_model: IKeypadModel
    view: ICalculationView
    _subject: ISubject

    def __post_init__(self) -> None:
        """Post init."""
        # Subscribe to model notifications
        self.model.subject.add_listener(self)

        # Subscribe to keypad notifications
        self.keypad_model.subscribe(FieldID.USER_INPUT, listener=self)
        self.view.keypad.subscribe(listener=self)

        # Subscribe to view notifications
        self.view.button_handler.add_listener(self)

    def on_open(self) -> None:
        """Initialize exercise when view becomes visible."""
        self.clear_page()
        self.model.start_exercise()

    # Listening for Model notifications by UI Name

    @property
    def fields(self) -> dict[FieldID, IStateSubject]:
        """Get the UI for a page event to manage its state."""
        return {
            FieldID.QUESTION_TEXT: self.view.display_question,
            FieldID.USER_INPUT: self.view.display_answer,
            FieldID.RESULT_STATUS: self.view.display_info,
        }

    # Listening to View notification

    def handle_keypad_press(self, value: str) -> None:
        """Handle keypad button press and update the answer display."""
        self.keypad_model.change(value)

    def handle_button_press(self, value: str) -> None:
        """Handle button press and notify Subject."""
        match value:
            case TaskState.ANSWER_CHECKING:
                user_input = self.keypad_model.text
                self.model.handle_answer(user_input)

    # Listing to Model notifications

    def display_task(self, value: str) -> None:
        """Display the task."""
        self.view.display_question.change(value)

    def display_result(self, value: str) -> None:
        """Display user answer checking result."""
        self.view.display_info.change(value)

    def clear_page(self) -> None:
        """Clear page fields."""
        # Clear view fields
        for field in self.fields.keys():
            self.clear_field(field)

        # Clear keypad model input data
        self.keypad_model.clean()

    def match_notify(
        self,
        notify_id: NotifyID,
        field_id: FieldID,
        items: Iterable,
        value: str,
    ) -> None:
        """Handle notification events and update view accordingly."""
        match notify_id:
            case NotifyID.UI_FIELD_VALUE_UPDATED:
                self.change_field(field_id, value)

            case NotifyID.UI_PAGE_CLEARED:
                self.clear_page()

    def change_field(self, field: FieldID, value: str) -> None:
        """Change the text value for specified UI element."""
        if ui := self.fields.get(field):
            ui.change(value)

    def clear_field(self, field: FieldID) -> None:
        """Clear the text value in specified UI element."""
        if ui := self.fields.get(field):
            ui.clean()

    def navigate(self, nav_id: NavID) -> None:
        """Handle navigation request from view."""
        self.subject.notify('navigate', nav_id=nav_id)

    # Properties

    # The controller notifies the `navigator` about the `content`.
    @property
    def subject(self) -> ISubject:
        """Get the notification subject instance."""
        return self._subject

    @property
    def content(self) -> IContent:
        """Get the current view content."""
        return self.view.content

    # Special Methods

    def __repr__(self) -> str:
        """Return developer-friendly string representation."""
        return f'{self.__class__.__name__}'
