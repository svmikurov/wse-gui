"""Manages the logic for the authentication feature."""

from toga.sources import Listener

from wse.core.logger import setup_logger
from wse.core.navigation.navigator import Navigator
from wse.core.navigation.routes import Route
from wse.features.auth.model import UserModel
from wse.features.auth.view import LoginView

logger = setup_logger('features.auth.LoginController')


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
        self.model.add_listener(self)
        self.view.add_listener(self)

    async def handle_login(self, username: str, password: str) -> None:
        """Handel the submit login event."""
        await self.model.authenticate(username, password)

    def navigate(self, route: Route) -> None:
        """Navigate to a specified route."""
        self.navigator.navigate(route)
