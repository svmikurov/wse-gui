"""Foreign discipline DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from .index import IndexForeignViewABC, IndexForeignViewModelABC
from .index.state import IndexForeignViewModel
from .index.view import IndexForeignView
from .params import WordStudyParamsViewABC, WordStudyParamsViewModelABC
from .params.state import WordStudyData, WordStudyParamsViewModel
from .params.view import WordStudyParamsView
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

        # Word study
        binder.bind(StudyForeignViewModelABC, to=StudyForeignViewModel)
        binder.bind(StudyForeignViewABC, to=StudyForeignView)

        # Word study params
        binder.bind(WordStudyData, scope=SingletonScope)
        binder.bind(WordStudyParamsViewModelABC, to=WordStudyParamsViewModel)
        binder.bind(WordStudyParamsViewABC, to=WordStudyParamsView)
