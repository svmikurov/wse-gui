"""Provides base classes for MVC (Model-View-Controller) components."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

import toga

from wse.core.navigation.navigation_id import NavID
from wse.features.shared.enums import FieldID, StyleID
from wse.features.shared.enums.notify_id import NotifyID
from wse.interfaces.ifeatures.icontent import IContent
from wse.interfaces.ifeatures.imvc import IModel, IView
from wse.interfaces.iobserver import IStateSubject, ISubject, ISubjectWithID
from wse.interfaces.iui.ibutton import IButtonHandler


@dataclass
class BaseModel:
    """Abstract base model implementing core MVC model functionality."""

    _subject: ISubjectWithID

    # === Lifecycle Methods ===
    def on_open(self) -> None:
        """Initialize model state when component is opened."""
        raise NotImplementedError(
            'Subclasses must implement the "on_open" method'
        )

    # === Properties ===
    @property
    def subject(self) -> ISubject:
        """Get the model's subject instance."""
        return self._subject


class ModelNotifyMixin:
    """Mixin to observer notification with ID."""

    subject: ISubject

    # === UI Notification Methods ===
    def notify_field_changed(self, filed: FieldID, value: str) -> None:
        """Notify observers to update a filed text value."""
        self.subject.notify(
            NotifyID.UI_FIELD_VALUE_UPDATED,
            field=filed,
            value=value,
        )

    def notify_field_cleared(self, field: FieldID) -> None:
        """Notify observers to clear a filed text value."""
        self.subject.notify(
            NotifyID.UI_FIELD_CLEARED,
            field=field,
        )


@dataclass
class BaseView(ABC):
    """Abstract base view implementing core MVC view functionality."""

    _content: IContent
    _style_config: dict[StyleID, dict]
    _button_handler: IButtonHandler

    def __post_init__(self) -> None:
        """Initialize view components after instance creation."""
        self._layout_view()

    def _layout_view(self) -> None:
        """Execute complete view setup sequence."""
        self._create_ui()
        self._populate_content()
        self.update_ui_style()
        self.localize_ui()

    # Abstract methods

    @abstractmethod
    def _populate_content(self) -> None:
        """Populate view with content."""

    @abstractmethod
    def _create_ui(self) -> None:
        """Create and configure view UI components."""

    @abstractmethod
    def localize_ui(self) -> None:
        """Localize all user-facing text in the view."""

    # Style Management

    @property
    @abstractmethod
    def _ui_styles(self) -> dict[toga.Widget, StyleID]:
        """Get mapping of widgets to their style IDs."""

    def update_ui_style(self) -> None:
        """Apply current style configuration to all view widgets."""
        for widget, style_id in self._ui_styles.items():
            widget.style.update(**self._style_config.get(style_id))

    # Properties

    @property
    def content(self) -> IContent:
        """Get the current content displayed in the view."""
        return self._content

    @property
    def button_handler(self) -> IButtonHandler:
        """Get the button handler."""
        return self._button_handler

    # UI creation methods
    def _create_nav_btn(self) -> toga.Button:
        """Create a standardized navigation button."""
        return toga.Button(on_press=self.button_handler.navigate)


@dataclass
class ViewController(ABC):
    """Abstract base view controller."""

    view: IView
    _subject: ISubject

    def __post_init__(self) -> None:
        """Initialize controller and set up view subscriptions."""
        self.view.button_handler.add_listener(self)

    # === View Event Handling ===
    def navigate(self, nav_id: NavID) -> None:
        """Handle navigation request from view."""
        self._subject.notify('navigate', nav_id=nav_id)

    # === Properties ===
    @property
    def subject(self) -> ISubject:
        """Get the notification subject instance."""
        return self._subject

    @property
    def content(self) -> IContent:
        """Get the current view content."""
        return self.view.content

    # === Special Methods ===
    def __repr__(self) -> str:
        """Return developer-friendly string representation."""
        return f'{self.__class__.__name__}'

    def __str__(self) -> str:
        """Return string representation."""
        return f'{self.__class__.__name__}'


@dataclass
class ModelViewController(ViewController, ABC):
    """Extended base controller with model integration."""

    model: IModel

    def __post_init__(self) -> None:
        """Initialize controller with model support."""
        super().__post_init__()
        self.model.subject.add_listener(self)

    # === Lifecycle Methods ===
    @abstractmethod
    def on_open(self) -> None:
        """Initialize controller state when component is opened."""
        raise NotImplementedError(
            'Subclasses must implement the "on_open" method'
        )

    # === UI State Management ===
    @property
    def fields(self) -> dict[FieldID, IStateSubject]:
        """Get the UI for a page event to manage its state."""
        raise NotImplementedError(
            'Subclasses must implement the "state_ui" property'
        )

    def change_field(self, field: FieldID, value: str) -> None:
        """Change the text value for specified UI element."""
        if ui := self.fields.get(field):
            ui.change(value)

    def clear_field(self, field: FieldID) -> None:
        """Clear the text value in specified UI element."""
        if ui := self.fields.get(field):
            ui.clean()
