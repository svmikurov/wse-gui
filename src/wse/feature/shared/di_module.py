"""Defines shared features injection module."""

from typing import no_type_check

from injector import Binder, Module

from ..interfaces.icontent import ContentProto
from ..interfaces.iobserver import SubjectABC
from . import Content, Subject


class FeatureSharedModule(Module):
    """Shared feature injection module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(ContentProto, to=Content)
        binder.bind(SubjectABC, to=Subject)
