"""Foreign discipline DI module."""

from typing import no_type_check

from injector import Binder, Module

from .index import IndexForeignViewABC, IndexForeignViewModelABC
from .index.state import IndexForeignViewModel
from .index.view import IndexForeignView
from .study import StudyForeignViewABC, StudyForeignViewModelABC
from .study.state import StudyForeignViewModel
from .study.view import StudyForeignView


class ForeignModule(Module):
    """Foreign discipline DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # Index
        binder.bind(IndexForeignViewModelABC, to=IndexForeignViewModel)
        binder.bind(IndexForeignViewABC, to=IndexForeignView)

        # Words study
        binder.bind(StudyForeignViewModelABC, to=StudyForeignViewModel)
        binder.bind(StudyForeignViewABC, to=StudyForeignView)
