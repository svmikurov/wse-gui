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

    HOME = Route('Home', 'main', 'home_controller')
    LOGIN = Route('Login', 'user', 'login_controller')
    EXERCISES = Route('Exercises', 'exercise', 'exercises_controller')
