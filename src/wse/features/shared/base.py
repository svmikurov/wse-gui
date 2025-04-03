"""Defines base classes of functions features."""

from abc import ABC
from dataclasses import dataclass

from wse.interface.ifeatures import IController, IModel, IView


@dataclass
class BaseController(IController, ABC):
    """Implementation of the base controller."""

    view: IView
    model: IModel | None = None

    def __post_init__(self) -> None:
        """Add sources."""
        self.view.subject.add_listener(self)
        if self.model:
            self.model.subject.add_listener(self)
