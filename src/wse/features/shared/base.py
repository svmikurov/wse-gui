"""Defines base classes of functions features."""

from dataclasses import dataclass

import toga

from wse.core.navigaion.navigation_id import NavigationID
from wse.features.shared.base_ui import BaseContent
from wse.features.shared.observer import Subject
from wse.interface.ifeatures import IContent, IModel, IView
from wse.pages.widgets import AppButton


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
    def navigate(self, button_text: NavigationID) -> None:
        """Navigate to page, the button event listener."""
        self._subject.notify('navigate', button_text=button_text)

    @property
    def subject(self) -> Subject:
        """Ger subject of observer."""
        return self._subject


class BaseView:
    """Implementation of the base controller."""

    _label_title: toga.Label

    def __init__(self, content_box: BaseContent | None) -> None:
        """Construct the view."""
        self._content = content_box or toga.Box()

        # Listeners
        self._subject = Subject()

    # Utility methods
    def _create_nav_btn(self) -> toga.Button:
        return AppButton(on_press=self._navigate)

    @property
    def subject(self) -> Subject:
        """Return the subject (read-only)."""
        return self._subject

    @property
    def title(self) -> str:
        """Page title (read-only)."""
        return self._label_title.text

    @property
    def content(self) -> BaseContent:
        """Page content (read-only)."""
        return self._content

    # Notifications
    def _navigate(self, button: toga.Button) -> None:
        self.subject.notify('navigate', button_text=button.text)
