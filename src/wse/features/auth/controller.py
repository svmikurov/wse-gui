"""Manages the logic for the authentication feature."""

from toga.sources import Listener

from wse.features.auth.model import UserModel
from wse.features.auth.view import LoginView


class LoginController(Listener):
    """Login screen controller."""

    def __init__(self, model: UserModel, view: LoginView) -> None:
        """Construct the controller."""
        self.model = model
        self.view = view

    def handel_login(self) -> None:
        """Handel the submit login event."""
        print('Login event')
