"""Defines Main Math page controller."""

from dataclasses import dataclass

from injector import inject

from wse.features.base import BaseController

from .interfaces import IIndexMathView


@inject
@dataclass
class IndexMathController(BaseController):
    """Main Math page controller."""

    _view: IIndexMathView
