"""Defines Home page controller."""

from dataclasses import dataclass

from injector import inject

from wse.features.base import BaseController

from .interfaces import IHomeView


@inject
@dataclass
class HomeController(BaseController):
    """Home page controller."""

    _view: IHomeView
