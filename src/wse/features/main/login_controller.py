"""Defines login page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from typing_extensions import override

from wse.features.base import mvc

if TYPE_CHECKING:
    from wse.features.main import LoginView

logger = logging.getLogger(__name__)


@dataclass
class LoginController(mvc.BaseContextController):
    """Login page controller."""

    view: LoginView

    @override
    def __post_init__(self) -> None:
        """Subscribe the controller to listen to login container."""
        super().__post_init__()
        self.view.login_container.subject.add_listener(self)

    # Listener methods
    def submit_login(self) -> None:
        """Submit the login, button handler."""
        logger.debug('The "Submit" button has been pressed to login')
