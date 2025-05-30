"""Defines the controller for the Multiplication Exercise page."""

from dataclasses import dataclass

from wse.core.navigation.navigation_id import NavID
from wse.features.mathem.interfaces.ipages import (
    ICalculationController,
    ICalculationModel,
    ICalculationView,
)
from wse.features.shared.enums import FieldID, TaskState
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
        self.keypad_model.add_listener(listener=self)
        self.view.keypad.add_listener(listener=self)

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
        self.view.display_question.clean()
        self.view.display_answer.clean()
        self.view.display_info.clean()

        # Clear keypad model input data
        self.keypad_model.clear()

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
