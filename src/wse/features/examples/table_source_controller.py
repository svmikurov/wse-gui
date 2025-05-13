from dataclasses import dataclass

from wse.core.navigation.navigation_id import NavID
from wse.interfaces.ifeatures.icontent import IContent
from wse.interfaces.ifeatures.imvc import IView
from wse.interfaces.iobserver import ISubject


@dataclass
class TableSourceContainer:
    """Selection example page controller."""

    view: IView
    _subject: ISubject

    def __post_init__(self) -> None:
        """Post init."""
        self.view.button_handler.add_listener(self)

    def on_open(self) -> None:
        """Call methods on page open event."""
        pass

    # -=== Listening to View notification ===-

    def navigate(self, nav_id: NavID) -> None:
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
