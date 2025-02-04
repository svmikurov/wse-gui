"""MVC instances factory."""

from dataclasses import dataclass
from typing import Type, TypeVar

import toga
from toga.sources import Listener, Source

from wse import contr, model, page

ModelT = Type[Source]
ViewT = Type[toga.Box]
ContrT = TypeVar('ContrT', bound=Listener)


@dataclass
class MVCData:
    """MVC model instances data class."""

    model_instance: str
    model_class: ModelT
    view_instance: str
    view_class: ViewT
    contr_instance: str
    contr_class: ContrT


class MVCFactory:
    """Factory of MVC model instances to initialize."""

    def __init__(self) -> None:
        """Construct the factory."""
        self._mvc_collection = []

    def add_mvc(
        self,
        model_instance: str,
        model_class: ModelT,
        view_instance: str,
        view_class: ViewT,
        contr_instance: str,
        contr_class: ContrT,
    ) -> None:
        """Add model-controller-view."""
        instance = MVCData(
            model_instance,
            model_class,
            view_instance,
            view_class,
            contr_instance,
            contr_class,
        )
        self._mvc_collection.append(instance)

    def initialize(self, cls: Type) -> None:
        """Initialize the MVC model instances."""
        for mvc in self._mvc_collection:
            setattr(cls, mvc.model_instance, mvc.model_class())
            setattr(cls, mvc.view_instance, mvc.view_class())
            model = getattr(cls, mvc.model_instance)
            view = getattr(cls, mvc.view_instance)
            setattr(cls, mvc.contr_instance, mvc.contr_class(model, view))


factory = MVCFactory()
# flake8: noqa: E501
# fmt: off
factory.add_mvc(
    'model_main', model.MainModel,
    'page_main', page.MainPage,
    'contr_main', contr.MainContr,
)
factory.add_mvc(
    'model_mult', model.TaskModel,
    'page_mult', page.MultPage,
    'contr_mult', contr.MultContr,
)
# fmt: on
