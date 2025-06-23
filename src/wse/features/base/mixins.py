"""Defines mixins for features base classes."""

import logging

from toga.style import Pack

from wse.features.interfaces import ISubject
from wse.features.interfaces.iwidgets import INavButton
from wse.features.shared.buttons import NavButton
from wse.features.subapps.nav_id import NavID

logger = logging.getLogger('wse')


class CreateNavButtonMixin:
    """Mixin that provides navigation button creation functionality."""

    _subject: ISubject

    def _create_nav_btn(self, nav_id: NavID) -> INavButton[Pack]:
        """Create navigation button."""
        return NavButton(nav_id=nav_id, on_press=self._handle_navigate)

    def _handle_navigate(self, button: INavButton[Pack]) -> None:
        """Handle navigation button press."""
        self._subject.notify('navigate', nav_id=button.nav_id)


class AddObserverMixin:
    """Mixin that enables observer subscription capability."""

    _subject: ISubject

    def add_observer(self, observer: object) -> None:
        """Subscribe observer an event has occurred."""
        self._subject.add_observer(observer)
