"""Protocols for math feature interfaces (Model-View-Controller)."""

from typing import Iterable, Protocol

import toga

from wse.core.navigation.navigation_id import NavID
from wse.features.mathem.interfaces.iexercise import IExerciseSwitcher
from wse.features.mathem.interfaces.isubjects import (
    ICalculationSubject,
    IMathematicalSubject,
)
from wse.features.mathem.sources import ExerciseSource
from wse.features.shared.enums import FieldID, StyleID
from wse.features.shared.enums.exercises import Exercises
from wse.features.shared.enums.notify_id import NotifyID
from wse.interface.iexercise import (
    IAnswerChecker,
    ITaskStorage,
    ITextDisplayRenderer,
)
from wse.interface.ifeatures.icontent import IContent
from wse.interface.iobserver import IStateSubject, ISubject
from wse.interface.iui.ibutton import IButtonHandler
from wse.interface.iui.ikeypad import IKeypad, IKeypadModel

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off

# Mathematical page

class IMathematicalModel(Protocol):
    """Protocol for math home page model."""
    _subject: IMathematicalSubject
    _exercise_switcher: IExerciseSwitcher

    # Mandatory protocols
    def on_open(self) -> None:
        """Initialize model state when component is opened."""

    # Optional protocols
    @property
    def subject(self) -> IMathematicalSubject:
        """Get the model's subject instance."""

    # Specific protocols
    @property
    def exercises_source(self) -> ExerciseSource:
        """Get exercises source instance."""
    def switch_exercise_type(self, exercise_type: Exercises) -> None:
        """Switch the current exercise type."""
    def update_default_exercise(self, value: str) -> None:
        """Update default exercise."""
    @property
    def _current_exercise_name(self) -> Exercises:
        """Get current exercise."""
    def _populate_selection_source(self) -> None:
        """Populate selection source and notify listeners."""
    def _get_source_item(self, name: Exercises) -> object:
        """Get from source the exercise DTO by its name."""
    def _notify_set_default_exercise(self) -> None:
        """Notify the controller to set the default exercise."""

class IMathematicalView(Protocol):
    """Protocol for math home page view."""
    exercise_selection: IStateSubject

    # Mandatory protocols
    # Layout
    def _layout_view(self) -> None: ...
    def _populate_content(self) -> None: ...
    def _create_ui(self) -> None: ...
    def localize_ui(self) -> None: ...
    def update_ui_style(self) -> None: ...
    @property
    def _ui_styles(self) -> dict[toga.Widget, StyleID]: ...
    # Other
    @property
    def content(self) -> IContent: ...
    @property
    def button_handler(self) -> IButtonHandler: ...
    def _create_nav_btn(self) -> toga.Button: ...

    # Optional protocols
    @property
    def subject(self) -> ISubject: ...

    # Specific protocols
    def switch_exercise(self, widget: toga.Selection) -> None:
        """Notify that exercise selected with selection UI."""

class IMathematicalController(Protocol):
    """Protocol for math home page controller."""
    model: IMathematicalModel
    view: IMathematicalView
    _subject: ISubject

    # Mandatory protocols
    def on_open(self) -> None:
        """Initialize controller state when component is opened."""
    @property
    def content(self) -> IContent: ...
    def navigate(self, nav_id: NavID) -> None:
        """Handle navigation request from view."""
    def __repr__(self) -> str:
        """Return developer-friendly string representation."""

    # Optional protocols
    @property
    def subject(self) -> ISubject:
        """Get the notification subject instance."""
    @property
    def fields(self) -> dict[FieldID, IStateSubject]:
        """Get the UI for a page event to manage its state."""
    def temporarily_disable(self, action: str, field_id: FieldID) -> None:
        """Disable temporarily the ui notification."""

    # Specific protocols
    def set_default_selection(self, value: str) -> None:
        """Set into selection ui the default exercise."""
    def switch_exercise(self, value: Exercises) -> None:
        """Change exercise."""

# Calculation page

class ICalculationModel(Protocol):
    """Protocol for math calculation page model."""
    exercise_switcher: IExerciseSwitcher
    storage: ITaskStorage
    render: ITextDisplayRenderer
    checker: IAnswerChecker
    _subject: ICalculationSubject

    # Mandatory protocols
    @property
    def subject(self) -> ICalculationSubject:
        """Get the model's subject instance."""

    # Specific protocols
    def start_exercise(self) -> None:
        """Start new exercise task."""
    def handle_answer(self, user_input: str) -> None:
        """Process user answer."""

class ICalculationView(Protocol):
    """Protocol for math calculation page view."""
    display_question: IStateSubject
    display_answer: IStateSubject
    display_info: IStateSubject
    keypad: IKeypad

    # Mandatory protocols
    # Layout
    def _layout_view(self) -> None: ...
    def _populate_content(self) -> None: ...
    def _create_ui(self) -> None: ...
    def localize_ui(self) -> None: ...
    def update_ui_style(self) -> None: ...
    @property
    def _ui_styles(self) -> dict[toga.Widget, StyleID]: ...
    # Other
    @property
    def content(self) -> IContent: ...
    @property
    def button_handler(self) -> IButtonHandler: ...
    def _create_nav_btn(self) -> toga.Button: ...

    # Optional protocols
    def _create_button(self) -> toga.Button: ...

class ICalculationController(Protocol):
    """Protocol for math calculation page controller."""
    model: ICalculationModel
    keypad_model: IKeypadModel
    view: ICalculationView
    _subject: ISubject

    # Mandatory protocols
    def on_open(self) -> None:
        """Initialize controller state when component is opened."""
    @property
    def content(self) -> IContent:
        """Get the current view content."""
    def navigate(self, nav_id: NavID) -> None:
        """Handle navigation request from view."""
    def __repr__(self) -> str:
        """Return developer-friendly string representation."""

    # Optional protocols
    @property
    def subject(self) -> ISubject:
        """Get the notification subject instance."""
    # Universal field notification methods
    @property
    def fields(self) -> dict[FieldID, IStateSubject]:
        """Get the UI for a page event to manage its state."""
    def match_notify(
        self,
        notify_id: NotifyID,
        field_id: FieldID,
        items: Iterable,
        value: str,
    ) -> None:
        """Handle notification events and update view accordingly."""
    def change_field(self, field: FieldID, value: str) -> None:
        """Change the text value for specified UI element."""
    def clear_field(self, field: FieldID) -> None:
        """Clear the text value in specified UI element."""
    # Button handler methods
    def handle_keypad_press(self, value: str) -> None:
        """Handle keypad button press and update the answer display."""
    def handle_button_press(self, value: str) -> None:
        """Handle button press and notify Subject."""

    # Specific protocols
    def display_task(self, value: str) -> None: ...
    def display_result(self, value: str) -> None: ...
    def clear_page(self) -> None: ...
