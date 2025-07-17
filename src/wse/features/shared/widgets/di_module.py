"""Defines widget injection module."""

from typing import Type

from injector import Module, provider, singleton

from .box_stub import FlexColumnStub, FlexRowStub
from .divider import Divider
from .interfaces import IDivider, IFlexColumnStub, IFlexRowStub


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
        """Provide column flex stub."""
        return FlexColumnStub

    @singleton
    @provider
    def provide_flex_row_stub(self) -> Type[IFlexRowStub]:
        """Provide row flex stub."""
        return FlexRowStub
