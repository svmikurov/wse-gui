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

    model_instance: str
    model_class: ModelT
    view_instance: str
    view_class: ViewT
    contr_instance: str
    contr_class: ContrT


class MVCFactory:
    """Factory of models-controller-view instances."""

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
        """Add models-controller-view."""
        instance = MVCData(
            model_instance,
            model_class,
            view_instance,
            view_class,
            contr_instance,
            contr_class,
        )
        self._mvc_collection.append(instance)

    def initialize(self, obj: toga.App) -> None:
        """Initialize the MVC models instances."""
        for mvc in self._mvc_collection:
            setattr(obj, mvc.model_instance, mvc.model_class())
            setattr(obj, mvc.view_instance, mvc.view_class())
            model = getattr(obj, mvc.model_instance)
            view = getattr(obj, mvc.view_instance)
            setattr(obj, mvc.contr_instance, mvc.contr_class(model, view))


factory = MVCFactory()
# fmt: off
factory.add_mvc(
    'model_main', models.MainModel,
    'page_main', pages.MainPage,
    'contr_main', controllers.MainContr,
)
factory.add_mvc(
    'model_mult', models.TaskModel,
    'page_mult', pages.MultPage,
    'contr_mult', controllers.MultContr,
)
# fmt: on
