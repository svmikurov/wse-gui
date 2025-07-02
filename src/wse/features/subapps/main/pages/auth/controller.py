"""Defines Authentication page controller."""

from dataclasses import dataclass

from injector import inject

from wse.features.base.mvc import BasePageController

from .interfaces import IAuthController, IAuthView


@inject
@dataclass
class AuthController(
    BasePageController,
    IAuthController,
):
    """Authentication page controller."""

    _view: IAuthView
