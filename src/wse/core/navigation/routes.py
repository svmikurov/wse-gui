"""Defines routes for application navigation."""

from dataclasses import dataclass


@dataclass
class Route:
    """Represents a route to a specific screen."""

    name: str
    controller_factory: str


class Routes:
    """Stores predefined routes for the application."""

    HOME: Route = Route('Home', 'home_controller')
    LOGIN: Route = Route('Login', 'login_controller')
