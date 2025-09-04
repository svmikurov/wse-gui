"""Defines widget injection module."""

from typing import Type

from injector import Module, provider, singleton

from . import DividerProto, FlexColumnStubProto, FlexRowStubProto
from .box_stub import FlexColumnStub, FlexRowStub
from .divider import Divider


class WidgetsModule(Module):
    """Widgets injection module."""

    @singleton
    @provider
    def provide_divider(self) -> Type[DividerProto]:
        """Provide divider."""
        return Divider

    @singleton
    @provider
    def provide_flex_column_stub(self) -> Type[FlexColumnStubProto]:
        """Provide column flex stub."""
        return FlexColumnStub

    @singleton
    @provider
    def provide_flex_row_stub(self) -> Type[FlexRowStubProto]:
        """Provide row flex stub."""
        return FlexRowStub
