"""Main pages controller."""

from typing import TypeVar

import toga
from toga.sources import Source

from wse.constants import HOST
from wse.controllers.base import BaseContr

ModelT = TypeVar('ModelT', bound=Source)
ViewT = TypeVar('ViewT', bound=toga.Box)


class MainContr(BaseContr):
    """Main pages controller."""

    _welcome = f'Ready for connect to {HOST}'

    def __init__(self, model: ModelT, view: ViewT) -> None:
        """Construct the controller."""
        super().__init__(model, view)

        self._view.btn_logout.on_press = self.logout
        self._view.btn_logout_cancel.on_press = self.cancel_logout
        self._view.btn_logout_confirm.on_press = self.confirm_logout

    async def on_open(self, _: toga.Widget) -> None:
        """Invoke methods on pages open."""
        self._update_widgets()

    ###################################################################
    # Button handlers

    def logout(self, _: toga.Button) -> None:
        """Logout."""
        self._place_logout_confirm()

    def confirm_logout(self, _: toga.Button) -> None:
        """Confirm logout."""
        self._model.logout()
        # TODO: delegate management to model notifications.
        self._update_widgets()

    def cancel_logout(self, _: toga.Button) -> None:
        """Cancel logout."""
        self._place_logout_button()

    ###################################################################
    # View management

    ###############
    # Place widgets

    def _update_widgets(self) -> None:
        """Update widgets by user auth status."""
        if self._model.is_auth:
            self._place_logout_button()
            self._display_userdata()
        else:
            self._place_login_button()
            self._display_greetings()

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

    ##############
    # Display text
    # TODO: delegate management to model notifications.

    def _display_userdata(self) -> None:
        self._view.info_panel.value = 'Добро пожаловать, {}!'.format(
            self._model.username
        )

    def _display_greetings(self) -> None:
        self._view.info_panel.value = self._welcome
