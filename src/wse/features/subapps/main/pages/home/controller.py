"""Defines Home page controller."""

from dataclasses import dataclass

from injector import inject

from wse.features.base.mvc import BasePageController

from .interfaces import IHomeController, IHomeView


@inject
@dataclass
class HomeController(
    BasePageController,
    IHomeController,
):
    """Home page controller."""

    _view: IHomeView
