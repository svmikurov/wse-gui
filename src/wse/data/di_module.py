"""Data layer DI module.

Note:
----
    Created for academic purposes.

"""

from typing import no_type_check

from injector import Binder, Module

from .task_data import (
    ExerciseDataSource,
    TaskDataRepository,
    TaskNetworkDataSource,
)


class DataModule(Module):
    """Data layer DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(ExerciseDataSource)
        binder.bind(TaskNetworkDataSource)
        binder.bind(TaskDataRepository)
