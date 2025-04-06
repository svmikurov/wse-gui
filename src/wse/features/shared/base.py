"""Defines base classes of functions features."""

from dataclasses import dataclass

from wse.core.navigaion.navigator import navigator
from wse.features.shared.button_text import ButtonText
from wse.interface.ifeatures import IContent, IController, IModel, IView


@dataclass
class BaseController(IController):
    """Implementation of the base controller."""

    view: IView
    model: IModel | None = None

    def __post_init__(self) -> None:
        """Add sources."""
        self.view.subject.add_listener(self)
        if self.model:
            self.model.subject.add_listener(self)

    @property
    def content(self) -> IContent:
        """Return page content."""
        return self.view.content

    @staticmethod
    def navigate(button_text: ButtonText) -> None:
        """Navigate to page, the button event listener."""
        navigator.navigate(button_text)
