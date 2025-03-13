"""Manages the logic for the main feature."""

from __future__ import annotations

from typing import TYPE_CHECKING

from toga.sources import Listener

from wse.core.navigation.routes import Route
from wse.features.auth.model import UserModel
from wse.features.main.view import HomeView

if TYPE_CHECKING:
    from wse.core.navigation.navigator import Navigator


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
        self.view.subject.add_listener(self)

    def navigate(self, route: Route) -> None:
        """Handel the exercises button press event."""
        self.navigator.navigate(route)
