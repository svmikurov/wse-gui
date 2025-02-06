"""Main pages controller."""

from typing import TypeVar

import toga
from toga.sources import Listener, Source

from wse.constants import HOST

ModelT = TypeVar('ModelT', bound=Source)
ViewT = TypeVar('ViewT', bound=toga.Box)


class MainContr(Listener):
    """Main pages controller."""

    _welcome = f'Ready for connect to {HOST}'

    def __init__(self, model: ModelT, view: ViewT) -> None:
        """Construct the controller."""
        self._model = model
        if self._model:
            self._model.add_listener(self)

        self._view = view
        self._view.set_controller(self)
        self._view.btn_logout.on_press = self.logout

    async def on_open(self, _: toga.Widget) -> None:
        """Invoke methods on pages open."""
        self._update_widgets()

    def logout(self, _: toga.Widget) -> None:
        """Logout."""
        self._model.logout()
        self._update_widgets()

    ###################################################################
    # View management methods

    def _update_widgets(self) -> None:
        """Update widgets by user auth status."""
        if self._model.is_auth:
            self._place_logout_button()
            self._display_userdata()
        else:
            self._place_login_button()
            self._display_greetings()

    def _place_login_button(self) -> None:
        self._view.box_auth_btn.clear()
        self._view.box_auth_btn.add(self._view.btn_goto_login)

    def _place_logout_button(self) -> None:
        self._view.box_auth_btn.clear()
        self._view.box_auth_btn.add(self._view.btn_logout)

    def _display_userdata(self) -> None:
        self._view.info_panel.value = 'Добро пожаловать, {}!'.format(
            self._model.username
        )

    def _display_greetings(self) -> None:
        self._view.info_panel.value = self._welcome
