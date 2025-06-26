"""Defines injection binds module container."""

from typing import no_type_check

from injector import Binder, Module

from wse.features.shared.containers.interfaces import ITextTaskPanel
from wse.features.shared.containers.task_panel import TextTaskPanel


class SharedContainersModule(Module):
    """Share container injection modules."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # MVC model
        binder.bind(ITextTaskPanel, to=TextTaskPanel)
