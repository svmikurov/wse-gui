"""Defines shared features injection module."""

from typing import no_type_check

from injector import Binder, Module

from ..interfaces.icontent import ContentProto
from ..interfaces.iobserver import Observable
from . import Content, Subject
from .views.integer.protocol import IntegerViewProto
from .views.integer.view import IntegerView


class FeatureSharedModule(Module):
    """Shared feature injection module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(ContentProto, to=Content)
        binder.bind(Observable, to=Subject)

        # Views
        binder.bind(IntegerViewProto, to=IntegerView)
