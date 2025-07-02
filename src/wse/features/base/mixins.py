"""Defines mixins for features base classes."""

import logging
from abc import ABC, abstractmethod

from wse.core.interfaces import INavigator

from ..interfaces import IContent, IObserver, ISubject
from ..interfaces.iwidgets import INavButton
from ..shared.widgets.buttons import NavButton
from ..subapps.nav_id import NavID

logger = logging.getLogger(__name__)


class BaseLocalizeMixin(ABC):
    """Mixin with provided `localize()` abstract method."""

    @abstractmethod
    def localize_ui(self) -> None:
        """Localize the UI text.

        For example:
            def localize_ui(self) -> None:
                self._label_title.text = label_('Home page title')
                ...
        """


class NavigateMixin:
    """Mixin to provide navigation functionality."""

    _navigator: INavigator

    def navigate(self, nav_id: NavID) -> None:
        """Navigate to page."""
        self._navigator.navigate(nav_id)


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

    def add_observer(self, observer: IObserver) -> None:
        """Subscribe observer an event has occurred."""
        self._subject.add_observer(observer)

    def _notify(self, notification: str, **kwargs: object) -> None:
        self._subject.notify(notification, **kwargs)


class CreateNavButtonMixin:
    """Mixin that provides navigation button creation functionality."""

    _subject: ISubject

    def _create_nav_btn(self, nav_id: NavID) -> INavButton:
        """Create navigation button."""
        return NavButton(nav_id=nav_id, on_press=self._handle_navigate)

    def _handle_navigate(self, button: INavButton) -> None:
        """Handle navigation button press."""
        self._subject.notify('navigate', nav_id=button.nav_id)
