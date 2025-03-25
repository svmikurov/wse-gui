"""Defines routes for application navigation."""

from dataclasses import dataclass


@dataclass
class Route:
    """Represents a route to a specific screen."""

    name: str
    feature: str
    controller_factory: str


class Routes:
    """Stores predefined routes for the application."""

    HOME: Route = Route('Home', 'main', 'home_controller')
    LOGIN: Route = Route('Login', 'user', 'login_controller')
    EXERCISES: Route = Route('Exercises', 'exercise', 'exercises_controller')
