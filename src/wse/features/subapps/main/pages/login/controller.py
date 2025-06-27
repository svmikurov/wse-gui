"""Defines Login page controller."""

from dataclasses import dataclass

from injector import inject

from wse.features.base.mvc import BasePageController
from wse.features.subapps.main.pages.login.interfaces import ILoginView


@inject
@dataclass
class LoginController(BasePageController):
    """Login page controller."""

    _view: ILoginView
