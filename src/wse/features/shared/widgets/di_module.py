"""Defines widget injection module."""

from typing import Type

from injector import Module, provider, singleton

from .box_stub import FlexColumnStub
from .divider import Divider
from .interfaces import IDivider, IFlexColumnStub


class WidgetsModule(Module):
    """Widgets injection module."""

    @singleton
    @provider
    def provide_divider(self) -> Type[IDivider]:
        """Provide divider."""
        return Divider

    @singleton
    @provider
    def provide_flex_column_stub(self) -> Type[IFlexColumnStub]:
        """Provide divider."""
        return FlexColumnStub
