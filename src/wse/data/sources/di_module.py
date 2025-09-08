"""Data sources DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from . import (
    TaskSource,
)


class SourceModule(Module):
    """Data sources DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(TaskSource, scope=SingletonScope)
