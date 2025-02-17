"""Main pages controller."""

from typing import TypeVar

import toga
from toga.sources import Source

from wse.controllers.base import BaseContr
from wse.models import User

ModelT = TypeVar('ModelT', bound=Source)
ViewT = TypeVar('ViewT', bound=toga.Box)


class HomeContr(BaseContr):
    """Main pages controller."""

    _user: User

    def __init__(self, model: ModelT, view: ViewT) -> None:
        """Construct the controller."""
        super().__init__(model, view)

        self._view.btn_logout.on_press = self.logout
        self._view.btn_logout_cancel.on_press = self.cancel_logout
        self._view.btn_logout_confirm.on_press = self.confirm_logout

    def on_open(self, _: toga.Widget) -> None:
        """Invoke methods on pages open."""
        self._user.on_open()

    ###################################################################
    # Button handlers

    def logout(self, _: toga.Button) -> None:
        """Logout."""
        self._place_logout_confirm()

    def confirm_logout(self, _: toga.Button) -> None:
        """Confirm logout."""
        self._user.logout()

    def cancel_logout(self, _: toga.Button) -> None:
        """Cancel logout."""
        self._place_logout_button()

    ###################################################################
    # Listener methods

    def place_auth_widgets(self) -> None:
        """Call methods if user is auth."""
        self._place_logout_button()

    def place_unauth_widgets(self) -> None:
        """Call methods if user is not auth."""
        self._place_login_button()

    def display_data(self, data: dict) -> None:
        """Display model data."""
        greetings = data.get('greetings')
        if greetings:
            self._display_greetings(greetings)

    ###################################################################
    # Place widgets

    def _clear_auth_box(self) -> None:
        self._view.box_auth_btn.clear()

    def _place_login_button(self) -> None:
        self._clear_auth_box()
        self._view.box_auth_btn.add(self._view.btn_goto_login)

    def _place_logout_button(self) -> None:
        self._clear_auth_box()
        self._view.box_auth_btn.add(self._view.btn_logout)

    def _place_logout_confirm(self) -> None:
        self._clear_auth_box()
        self._view.box_auth_btn.add(
            self._view.btn_logout_cancel, self._view.btn_logout_confirm
        )

    ###################################################################
    # Display data

    def _display_greetings(self, greetings: str) -> None:
        self._view.info_panel.value = greetings
