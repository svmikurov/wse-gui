"""Defines shared features injection container."""

from typing import no_type_check

from injector import Binder, Module

from ..interfaces import (
    IContent,
    ISubject,
)
from . import Content, Subject


class FeatureSharedModule(Module):
    """Shared feature injection container."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(IContent, to=Content)
        binder.bind(ISubject, to=Subject)
