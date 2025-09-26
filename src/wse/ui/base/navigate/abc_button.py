"""Base navigation button."""

from abc import ABC, abstractmethod

from wse.core.navigation import NavID
from wse.ui.base.iwidgets import NavigableButton
from wse.ui.widgets.buttons import NavButton


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
