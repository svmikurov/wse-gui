"""Mathematical feature controller (MVC)."""

import logging
from dataclasses import dataclass

from wse.core.navigation.navigation_id import NavID
from wse.features.mathem.interfaces.ipages import (
    IMathematicalController,
    IMathematicalModel,
    IMathematicalView,
)
from wse.features.shared.enums import FieldID
from wse.features.shared.enums.exercises import Exercises
from wse.interface.ifeatures.icontent import IContent
from wse.interface.iobserver import IStateSubject, ISubject

logger = logging.getLogger(__name__)


@dataclass
class MathematicalController(IMathematicalController):
    """Controller for mathematical exercises page."""

    model: IMathematicalModel
    view: IMathematicalView
    _subject: ISubject

    def __post_init__(self) -> None:
        """Construct the controller."""
        # Subscribe to model notifications
        self.model.exercises_source.add_listener(
            self.view.exercise_selection.items  # type: ignore
        )

        # Subscribe to view notifications
        self.view.button_handler.add_listener(self)
        self.view.subject.add_listener(self)

        # When updating widget data, it can call the
        # `on_change` method. While the widget data
        # is being updated, the method is disabled.
        self._disabled_widgets: dict = {}

    def on_open(self) -> None:
        """Initialize controller state when component is opened."""
        self.model.on_open()

    # Listening for Model notifications by UI Name

    @property
    def fields(self) -> dict[FieldID, IStateSubject]:
        """Get the UI for a page event to manage its state."""
        return {
            FieldID.EXERCISE_SELECTION: self.view.exercise_selection,
        }

    # Listing the Model notifications

    def set_default_selection(self, value: str) -> None:
        """Set into selection ui the default exercise."""
        self.view.exercise_selection.value = value

    def temporarily_disable(self, action: str, field_id: FieldID) -> None:
        """Disable temporarily the ui notification."""
        widget = self.fields[field_id]

        if action == 'disable':
            self._disabled_widgets[field_id] = widget._on_change
            widget.on_change = None  # type: ignore

        elif action == 'enable' and field_id in self._disabled_widgets:
            widget._on_change = self._disabled_widgets.pop(field_id)

    # Listing the View notifications

    def switch_exercise(self, value: Exercises) -> None:
        """Change exercise."""
        self.model.switch_exercise_type(value)
        logger.debug(f'Selected "{value}" exercise')

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
