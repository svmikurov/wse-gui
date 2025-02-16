"""MVC instances factory."""

from dataclasses import dataclass
from typing import Type, TypeVar

import toga
from toga.sources import Listener, Source

from wse import controllers, models, pages

ModelT = Type[Source]
ViewT = Type[toga.Box]
ContrT = TypeVar('ContrT', bound=Listener)


@dataclass
class MVCData:
    """MVC models instances data class."""

    model_attr_name: str
    model_class: ModelT | None
    view_attr_name: str
    view_class: ViewT
    contr_attr_name: str
    contr_class: ContrT


class MVCFactory:
    """Factory of models-controller-view instances."""

    def __init__(self) -> None:
        """Construct the factory."""
        self._mvc_collection = []

    def add(self, **kwargs: object) -> None:
        """Add programmatically models-controller-view."""
        attrs = []
        for item in kwargs.items():
            attrs.extend(item)
        self._mvc_collection.append(MVCData(*attrs))

    def initialize(self, obj: toga.App) -> None:
        """Initialize the MVC model instances."""
        # fmt: off
        for mvc in self._mvc_collection:
            model = (
                self._setattr(obj, mvc.model_attr_name, mvc.model_class())
                if mvc.model_class
                else None
            )
            view = self._setattr(
                obj, mvc.view_attr_name, mvc.view_class()
            )
            contr = self._setattr(
                obj, mvc.contr_attr_name, mvc.contr_class(model, view)
            )
            contr.set_user(obj.user)
        # fmt: on

    @staticmethod
    def _setattr(obj: object, name: str, value: object) -> object:
        setattr(obj, name, value)
        return getattr(obj, name)


mvc_factory = MVCFactory()
########################################################################
# Main

mvc_factory.add(
    model_main=None,
    page_main=pages.HomePage,
    contr_main=controllers.HomeContr,
)

########################################################################
# Foreign

...

########################################################################
# Glossary

...

########################################################################
# Mathematics

mvc_factory.add(
    model_calc=models.MultiplicationModel,
    page_calc=pages.CalcPage,
    contr_calc=controllers.CalcContr,
)
