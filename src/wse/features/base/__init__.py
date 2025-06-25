"""Defines base and abstract base classes for features."""

__all__ = [
    'BaseController',
    'BaseModel',
    'BaseRoutes',
    'BaseView',
]

from wse.features.base.mvc import BaseController, BaseModel, BaseView
from wse.features.base.routes import BaseRoutes
