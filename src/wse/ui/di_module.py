"""UI layer DI module."""

from typing import no_type_check

from injector import Binder, Module
from typing_extensions import override

from .base.content.abc import ContentABC
from .content import Content
from .routes import UIRoutes


class UIModule(Module):
    """UI layer DI module."""

    @no_type_check
    @override
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(ContentABC, to=Content)
        binder.bind(UIRoutes)
