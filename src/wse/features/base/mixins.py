"""Defines mixins for features base classes."""

import logging

import toga

from wse.features.interfaces import ISubject

logger = logging.getLogger('wse')


class CreateNavButtonMixin:
    """Mixin that provides navigation button creation functionality."""

    _subject: ISubject

    def _create_nav_btn(self) -> toga.Button:
        """Create navigation button."""
        return toga.Button(on_press=self._handle_navigate)

    def _handle_navigate(self, button: toga.Button) -> None:
        """Handle navigation button press."""
        self._subject.notify('navigate', nav_id=button.text)


class SubscribeObserverMixin:
    """Mixin that enables observer subscription capability."""

    _subject: ISubject

    def add_observer(self, observer: object) -> None:
        """Subscribe observer an event has occurred."""
        self._subject.add_observer(observer)
