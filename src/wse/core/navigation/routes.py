"""Application routes."""

from dataclasses import dataclass

from pydantic import BaseModel

from wse.features.auth.view import LoginView
from wse.features.main.view import HomeView
from wse.features.shared.view import BaseView


@dataclass
class Route:
    """Route to screen."""

    name: str
    view: BaseView


class Routes:
    """Routes to screen."""

    HOME: Route = Route('Home', HomeView)
    LOGIN: Route = Route('Login', LoginView)
