"""Defines shared features injection module."""

from typing import no_type_check

from injector import Binder, Module

from .observer.abc import SubjectABC
from .observer.subject import Subject
from .timer import TimerABC
from .timer.time import Timer


class FeatureSharedModule(Module):
    """Shared feature injection module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(SubjectABC, to=Subject)
        binder.bind(TimerABC, to=Timer)
