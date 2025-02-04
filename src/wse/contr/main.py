"""Main page controller."""

from typing import TypeVar

import toga
from toga.sources import Listener, Source

ModelT = TypeVar('ModelT', bound=Source)
ViewT = TypeVar('ViewT', bound=toga.Box)


class MainContr(Listener):
    """Main page controller."""

    def __init__(self, model: ModelT, view: ViewT) -> None:
        """Construct the controller."""
        self._model = model
        self._model.add_listener(self)

        self._view = view
