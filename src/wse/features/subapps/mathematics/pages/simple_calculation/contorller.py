"""Defines the controller of Simple Math calculation page."""

from dataclasses import dataclass

from injector import inject

from wse.features.base import BaseController

from .interfaces import ISimpleCalcView


@inject
@dataclass
class SimpleCalcController(BaseController):
    """The controller of Simple Math calculation page."""

    _view: ISimpleCalcView
