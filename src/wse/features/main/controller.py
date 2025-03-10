"""Manages the logic for the main feature."""

from __future__ import annotations

from typing import TYPE_CHECKING

from toga.sources import Listener

from wse.core.logger import setup_logger
from wse.features.auth.model import UserModel
from wse.features.main.view import HomeView

if TYPE_CHECKING:
    from wse.core.navigation.navigator import Navigator

logger = setup_logger('HomeController')


class HomeController(Listener):
    """Home screen controller."""

    def __init__(
        self,
        model: UserModel,
        view: HomeView,
        navigator: Navigator,
    ) -> None:
        """Construct the controller."""
        self.model = model
        self.view = view
        self.navigator = navigator
        self.view.add_listener(self)

    def handel_exercises(self) -> None:
        """Handel the exercises button press event."""
        logger.info('Call listener')
