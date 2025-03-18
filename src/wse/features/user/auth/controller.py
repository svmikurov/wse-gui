"""Manages the logic for the authentication feature."""

import logging

from toga.sources import Listener

from wse.core.navigation.navigator import Navigator
from wse.core.navigation.routes import Route
from wse.features.user.auth.model import UserModel
from wse.features.user.auth.view import LoginView

logger = logging.getLogger(__name__)


class LoginController(Listener):
    """Login screen controller."""

    def __init__(
        self,
        model: UserModel,
        view: LoginView,
        navigator: Navigator,
    ) -> None:
        """Construct the controller."""
        self.model = model
        self.view = view
        self.navigator = navigator
        self.model.subject.add_listener(self)
        self.view.subject.add_listener(self)

    ####################################################################
    # Listener methods

    async def handle_login(self, username: str, password: str) -> None:
        """Handel the submit login event."""
        await self.model.authenticate(username, password)

    def navigate(self, route: Route) -> None:
        """Navigate to a specified route."""
        self.navigator.navigate(route)

    def show_username_errors(self, errors: list[str]) -> None:
        """Show username errors on authenticate."""
        print(f'>>> username {errors = }')

    def show_password_errors(self, errors: list[str]) -> None:
        """Show password errors on authenticate."""
        print(f'>>> password {errors = }')

    def show_credentials_error(self, error: str) -> None:
        """Show credentials error on authenticate."""
        print(f'>>> credentials {error = }')
