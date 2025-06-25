"""Defines mixins for features base classes."""

import logging

from wse.features.interfaces import IContent, ISubject
from wse.features.interfaces.iwidgets import INavButton
from wse.features.shared.buttons import NavButton
from wse.features.subapps.nav_id import NavID

logger = logging.getLogger('__name__')


class GetContentMixin:
    """Mixin to provide content."""

    _content: IContent

    @property
    def content(self) -> IContent:
        """Get page content."""
        return self._content


class AddObserverMixin:
    """Mixin that enables observer subscription capability."""

    _subject: ISubject

    def add_observer(self, observer: object) -> None:
        """Subscribe observer an event has occurred."""
        self._subject.add_observer(observer)


class CreateNavButtonMixin:
    """Mixin that provides navigation button creation functionality."""

    _subject: ISubject

    def _create_nav_btn(self, nav_id: NavID) -> INavButton:
        """Create navigation button."""
        return NavButton(nav_id=nav_id, on_press=self._handle_navigate)

    def _handle_navigate(self, button: INavButton) -> None:
        """Handle navigation button press."""
        self._subject.notify('navigate', nav_id=button.nav_id)
