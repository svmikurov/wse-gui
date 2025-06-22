"""Defines abstract base classes for features."""

__all__ = [
    'BaseRoutes',
    'BaseView',
    'BaseController',
]

from wse.features.base.mvc import BaseController, BaseView
from wse.features.base.routes import BaseRoutes
