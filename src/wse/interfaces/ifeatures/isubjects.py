"""Defines interface for MVC model subject of Observer pattern."""

from typing import Protocol

from wse.features.shared.enums import FieldID
from wse.interfaces.iobserver import ISubject

# fmt: off


class IModelSubject(ISubject, Protocol):
    """Protocol for subjects that notify about model data changes."""
    def notify_data_changed(self, field: FieldID, value: object) -> None:
        """Notify observers about changed field value."""
    def notify_data_cleared(self, field: FieldID) -> None:
        """Notify observers about cleared field data."""
    def notify_page_cleared(self) -> None:
        """Notify observers about cleared page data."""
