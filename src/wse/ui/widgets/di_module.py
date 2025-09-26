"""Defines widget injection module."""

from injector import Module, provider, singleton

from . import DividerType, FlexColumnStubType, FlexRowStubType
from .box_stub import FlexColumnStub, FlexRowStub
from .divider import Divider


class WidgetsModule(Module):
    """Widgets injection module."""

    @singleton
    @provider
    def provide_divider(self) -> DividerType:
        """Provide divider."""
        return Divider

    @singleton
    @provider
    def provide_flex_column_stub(self) -> FlexColumnStubType:
        """Provide column flex stub."""
        return FlexColumnStub

    @singleton
    @provider
    def provide_flex_row_stub(self) -> FlexRowStubType:
        """Provide row flex stub."""
        return FlexRowStub
