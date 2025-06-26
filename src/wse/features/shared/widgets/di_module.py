"""Defines widget injection container."""

from typing import Callable

from injector import Module, provider, singleton

from .box_stub import FlexColumnStub
from .divider import Divider
from .interfaces import IDivider, IFlexColumnStub


class WidgetsModule(Module):
    """Widgets injection container."""

    @singleton
    @provider
    def provide_divider(self) -> Callable[[], IDivider]:
        """Provide divider."""
        return Divider

    @singleton
    @provider
    def provide_flex_column_stub(self) -> Callable[[], IFlexColumnStub]:
        """Provide divider."""
        return FlexColumnStub
