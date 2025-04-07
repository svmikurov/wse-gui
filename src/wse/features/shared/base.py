"""Defines base classes of functions features."""

from dataclasses import dataclass

from wse.features.shared.button_text import ButtonText
from wse.features.shared.observer import Subject
from wse.interface.ifeatures import IContent, IModel, ISubject, IView


@dataclass
class BaseController(Subject):
    """Implementation of the base controller."""

    view: IView
    model: IModel | None = None

    def __post_init__(self) -> None:
        """Add sources."""
        self._subject = Subject()
        self.view.subject.add_listener(self)
        if self.model:
            self.model.subject.add_listener(self)

    @property
    def content(self) -> IContent:
        """Return page content."""
        return self.view.content

    # Notifications
    def navigate(self, button_text: ButtonText) -> None:
        """Navigate to page, the button event listener."""
        self._subject.notify('navigate', button_text=button_text)

    @property
    def subject(self) -> ISubject:
        """Ger subject of observer."""
        return self._subject
