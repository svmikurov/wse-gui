"""Manages the logic for the authentication feature."""

from toga.sources import Listener

from wse.core.logger import setup_logger
from wse.core.navigation.navigator import Navigator
from wse.features.auth.model import UserModel
from wse.features.auth.view import LoginView

logger = setup_logger('LoginController')


class LoginController(Listener):
    """Login screen controller."""

    def __init__(
        self,
        model: UserModel,
        navigator: Navigator,
    ) -> None:
        """Construct the controller."""
        self.model = model
        self.navigator = navigator
        self.view = LoginView()
        self.view.add_listener(self)

    def handle_login(self) -> None:
        """Handel the submit login event."""
        logger.info('Call listener')
