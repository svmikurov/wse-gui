"""Abstract Base Classes for navigation."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from wse.core.navigation import NavID
from wse.feature.interfaces.iwidgets import NavigableButton
from wse.feature.shared.widgets.buttons import NavButton


class NavigateABC(ABC):
    """ABC for navigate feature."""

    @abstractmethod
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event."""


@dataclass
class CreateNavButtonABC(ABC):
    """ABC for navigable container.

    For example:

        self._btn_account = self._create_nav_btn(nav_id=NavID.ACCOUNT)

        1) Use with observer pattern:

        _subject: Observable

        def _handle_navigate(self, button: NavigableButton) -> None:
            self._subject.notify('navigate', nav_id=button.nav_id)

        2) Use with callback of ViewModel method:

        def _handle_navigate(self, button: NavigableButton) -> None:
            self._state.navigate(button.nav_id)
    """

    def _create_nav_btn(self, nav_id: NavID) -> NavigableButton:
        """Create navigation button."""
        return NavButton(nav_id=nav_id, on_press=self._handle_navigate)

    @abstractmethod
    def _handle_navigate(self, button: NavigableButton) -> None:
        """Handle navigation button press."""
