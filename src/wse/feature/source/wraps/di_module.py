"""Source wrap DI module."""

from typing import no_type_check

from injector import Binder, Module

from ..wraps import ExerciseSelectWrapperABC
from ..wraps.selection import ExerciseSelectSourceWrap


class SourceWrapsModule(Module):
    """Source wrap DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(ExerciseSelectWrapperABC, to=ExerciseSelectSourceWrap)
