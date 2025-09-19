"""UI containers DI module."""

from typing import no_type_check

from injector import Binder, Module

from .presentation import PresentationContainerABC
from .presentation.container import PresentationContainer


class UIContainerModule(Module):
    """UI containers DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # Presentation container
        binder.bind(PresentationContainerABC, to=PresentationContainer)
