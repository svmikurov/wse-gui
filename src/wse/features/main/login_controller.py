"""Defines login page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from typing_extensions import override

from wse.features.base import mvc

if TYPE_CHECKING:
    from wse.features.main import LoginModel, LoginView

logger = logging.getLogger(__name__)


@dataclass
class LoginController(mvc.ContextController):
    """Login page controller."""

    view: LoginView
    model: LoginModel

    @override
    def __post_init__(self) -> None:
        """Subscribe the controller to listen to log in container."""
        super().__post_init__()
        self.view.login_container.subject.add_listener(self)

    # Listener methods
    def submit_login(self, username: str, password: str) -> None:
        """Submit the login, button handler."""
        self.model.login(username, password)

    def clear_input_fields(self) -> None:
        """Clear a username and password fields."""
        self.view.login_container.clear_input_fields()
