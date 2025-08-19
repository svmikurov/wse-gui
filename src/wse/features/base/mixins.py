"""Defines mixins for features base classes."""

import logging
from dataclasses import dataclass
from typing import Any

from injector import inject

from wse.core.interfaces import INavigator

from ...apps.nav_id import NavID
from ..interfaces.icontent import IContent
from ..interfaces.iobserver import IObserver, ISubject
from ..interfaces.iwidgets import INavButton
from ..shared.widgets.buttons import NavButton

logger = logging.getLogger(__name__)


@inject
@dataclass
class NavigateMixin:
    """Mixin to provide navigation functionality."""

    _navigator: INavigator

    def navigate(self, nav_id: NavID, **kwargs: dict[str, Any]) -> None:
        """Navigate to page."""
        self._navigator.navigate(nav_id, **kwargs)


@inject
@dataclass
class NotifyNavigateMixin:
    """Mixin to provide navigation notification.

    Use to pass navigation event notification from view component to
    controller.
    To do this, add a mixin in the view component controller and the
    view controller.

    For example:

        class TopBarController(NotifyNavigateMixin, ...): ...

        class SomePageController((NotifyNavigateMixin, ...):

            _container: ITopBarController

    """

    _subject: ISubject

    def navigate(self, nav_id: NavID) -> None:
        """Notify to navigate."""
        self._subject.notify('navigate', nav_id=nav_id)


@inject
@dataclass
class CreateNavButtonMixin:
    """Mixin that provides navigation button creation functionality."""

    _subject: ISubject

    def _create_nav_btn(self, nav_id: NavID) -> INavButton:
        """Create navigation button."""
        return NavButton(nav_id=nav_id, on_press=self._handle_navigate)

    def _handle_navigate(self, button: INavButton) -> None:
        """Handle navigation button press."""
        self._subject.notify('navigate', nav_id=button.nav_id)


@inject
@dataclass
class GetContentMixin:
    """Mixin to provide content."""

    _content: IContent

    @property
    def content(self) -> IContent:
        """Get page content."""
        return self._content


@inject
@dataclass
class AddObserverMixin:
    """Mixin that enables observer subscription capability."""

    _subject: ISubject

    def add_observer(self, observer: IObserver) -> None:
        """Subscribe observer an event has occurred."""
        self._subject.add_observer(observer)

    def _notify(self, notification: str, **kwargs: object) -> None:
        self._subject.notify(notification, **kwargs)
