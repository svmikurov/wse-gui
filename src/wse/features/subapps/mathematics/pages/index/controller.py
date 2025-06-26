"""Defines Main Math page controller."""

from dataclasses import dataclass

from injector import inject

from wse.features.base.mvc import BasePageController

from .interfaces import IIndexMathView


@inject
@dataclass
class IndexMathController(BasePageController):
    """Main Math page controller."""

    _view: IIndexMathView
