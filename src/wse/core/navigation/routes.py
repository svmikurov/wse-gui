"""Defines routes for application navigation."""

from dataclasses import dataclass
from typing import Type

import toga

from wse.features.auth.view import LoginView
from wse.features.main.view import HomeView


@dataclass
class Route:
    """Represents a route to a specific screen."""

    name: str
    view: Type[toga.Box]


class Routes:
    """Stores predefined routes for the application."""

    HOME: Route = Route('Home', HomeView)
    LOGIN: Route = Route('Login', LoginView)
