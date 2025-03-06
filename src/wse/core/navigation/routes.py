"""Defines routes for application navigation."""

from dataclasses import dataclass

from wse.features.auth.view import LoginView
from wse.features.main.view import HomeView
from wse.features.shared.view import BaseView


@dataclass
class Route:
    """Represents a route to a specific screen."""

    name: str
    view: BaseView


class Routes:
    """Stores predefined routes for the application."""

    HOME: Route = Route('Home', HomeView)
    LOGIN: Route = Route('Login', LoginView)
