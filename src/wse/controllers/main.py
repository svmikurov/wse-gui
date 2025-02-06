"""Main pages controller."""

from typing import TypeVar

import toga
from toga.sources import Listener, Source

from wse.models.user import User

ModelT = TypeVar('ModelT', bound=Source)
ViewT = TypeVar('ViewT', bound=toga.Box)


class MainContr(Listener):
    """Main pages controller."""

    def __init__(self, model: ModelT, view: ViewT) -> None:
        """Construct the controller."""
        self._model = model
        self._model.add_listener(self)
        self._user: User | None = None

        self._view = view

    def set_user(self, user: User) -> None:
        """Set user instance to controller."""
        self._user = user
