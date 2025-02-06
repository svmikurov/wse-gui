"""Base controller."""

from typing import TypeVar

import toga
from toga.sources import Listener, Source

ModelT = TypeVar('ModelT', bound=Source)
ViewT = TypeVar('ViewT', bound=toga.Box)


class BaseContr(Listener):
    """Base controller."""

    def __init__(self, model: ModelT | None, view: ViewT) -> None:
        """Construct the controller."""
        self._view = None
        self._model = None
        self.set_model(model)
        self.set_view(view)

    def set_model(self, model: ModelT | None) -> None:
        """Set model."""
        self._model = model
        if self._model:
            self._model.add_listener(self)

    def set_view(self, view: ViewT) -> None:
        """Set view."""
        self._view = view
        self._view.set_controller(self)
