"""Protocol definitions for MVC (Model-View-Controller) components."""

from typing import Protocol

import toga

from wse.core.navigation.navigation_id import NavID
from wse.features.shared.enums import FieldID, StyleID
from wse.interface.ifeatures.icontent import IContent
from wse.interface.iobserver import IStateSubject, ISubject
from wse.interface.iui.ibutton import IButtonHandler

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off


class IModel(Protocol):
    """Protocol defining the interface for Model components."""
    _subject: ISubject
    def __post_init__(self) -> None:
        """Initialize model and subscribe to service notifications."""
    def on_open(self) -> None:
        """Initialize model state when component is opened."""
    @property
    def subject(self) -> ISubject:
        """Get the model's notification subject instance."""
    def notify_change_text(self, field: FieldID, value: str) -> None:
        """Notify observers to update a UI element's text value."""
    def notify_clean_text(self, field: FieldID) -> None:
        """Notify observers to clear a UI element's text value."""

class IView(Protocol):
    """Protocol defining the interface for View components."""
    _content: IContent
    _style_config: dict[StyleID, dict]
    button_handler: IButtonHandler
    def __post_init__(self) -> None:
        """Initialize view components after instance creation."""
    def _layout_view(self) -> None:
        """Execute complete view setup sequence."""
    def _populate_content(self) -> None:
        """Populate view with dynamic content."""
    def _create_ui(self) -> None:
        """Create and configure all UI components for the view."""
    def localize_ui(self) -> None:
        """Localize all user-facing text in the view components."""
    @property
    def _ui_styles(self) -> dict[toga.Widget, StyleID]:
        """Get style mapping for view widgets."""
    def update_ui_style(self) -> None:
        """Apply current style configuration to all view widgets."""
    @property
    def content(self) -> IContent:
        """Get the current content displayed in the view."""
    def _create_nav_btn(self) -> toga.Button:
        """Create a standardized navigation button."""

class IVController(Protocol):
    """Protocol defining the base View Controller interface."""
    view: IView
    _subject: ISubject
    def __post_init__(self) -> None:
        """Initialize controller and set up view subscriptions."""
    def navigate(self, nav_id: NavID) -> None:
        """Handle navigation request from view."""
    @property
    def subject(self) -> ISubject:
        """Get the controller's notification subject."""
    @property
    def content(self) -> IContent:
        """Get the current view content."""
    def __repr__(self) -> str:
        """Return developer-friendly string representation."""

class IMVController(IVController, Protocol):
    """Protocol extending IVController with Model integration."""
    model: IModel
    def __post_init__(self) -> None:
        """Initialize controller with model support."""
    def on_open(self) -> None:
        """Initialize controller state when component is opened."""
    @property
    def fields(self) -> dict[FieldID, IStateSubject]:
        """Get the page field to manage its state."""
    def change_ui_value(self, field: FieldID, value: str) -> None:
        """Change the page field for specified UI element."""
    def clean_ui_value(self, field: FieldID) -> None:
        """Clear the text value in specified UI element."""
