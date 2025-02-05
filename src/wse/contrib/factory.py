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
    model_class: ModelT
    view_attr_name: str
    view_class: ViewT
    contr_attr_name: str
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
        mvc = MVCData(
            model_instance,
            model_class,
            view_instance,
            view_class,
            contr_instance,
            contr_class,
        )
        self._mvc_collection.append(mvc)

    def initialize(self, obj: toga.App) -> None:
        """Initialize the MVC model instances."""
        for mvc in self._mvc_collection:
            model = self._setattr(obj, mvc.model_attr_name, mvc.model_class())
            view = self._setattr(obj, mvc.view_attr_name, mvc.view_class())
            setattr(obj, mvc.contr_attr_name, mvc.contr_class(model, view))

    @staticmethod
    def _setattr(obj: toga.App, name: str, value: ModelT | ViewT) -> object:
        setattr(obj, name, value)
        return getattr(obj, name)


mvc_factory = MVCFactory()
# fmt: off
mvc_factory.add_mvc(
    'model_main', models.MainModel,
    'page_main', pages.MainPage,
    'contr_main', controllers.MainContr,
)
mvc_factory.add_mvc(
    'model_mult', models.TaskModel,
    'page_mult', pages.MultPage,
    'contr_mult', controllers.MultContr,
)
# fmt: on
