"""Defines multiplication page model."""

import dataclasses
import logging

from wse.features import UIName
from wse.interface.ifeatures import IModel
from wse.interface.iobserver import ISubject
from wse.interface.iui.itext import IDisplayModel

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class MultiplicationModel(IModel):
    """Multiplication page model."""

    _subject: ISubject
    display_model: IDisplayModel
    display_input: IDisplayModel

    def __post_init__(self) -> None:
        """Subscribe to notifications."""
        self.display_model.set_ui_name('display_model')
        self.display_model.subject.add_listener(self)
        self.display_input.set_ui_name('display_input')
        self.display_input.subject.add_listener(self)

    # Context

    # TODO: remove from class?
    def render_context(self) -> None:
        """Render the context to view."""
        self._set_context()
        self._notify_render_context()

    def _set_context(self) -> None:
        """Set view context for render into view."""

    def _notify_render_context(self) -> None:
        """Notify controller to fill view with context."""

    # Notifications

    def change_ui_value(self, ui_name: UIName, value: str) -> None:
        """Change UI text value according UI name."""
        self.subject.notify('change_ui_value', ui_name=ui_name, value=value)

    def clean_ui_value(self, ui_name: UIName) -> None:
        """Change UI text value according UI name."""
        self.subject.notify('clean_ui_value', ui_name=ui_name)

    # Utility methods

    @property
    def subject(self) -> ISubject:
        """Model subject."""
        return self._subject
