"""Defines shared features injection module."""

from typing import no_type_check

from injector import Binder, Module

from ..interfaces.icontent import IContent
from ..interfaces.iobserver import ISubject
from . import Content, Subject


class FeatureSharedModule(Module):
    """Shared feature injection module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(IContent, to=Content)
        binder.bind(ISubject, to=Subject)
