"""Foreign discipline DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from .index import IndexForeignViewABC, IndexForeignViewModelABC
from .index.state import IndexForeignViewModel
from .index.view import IndexForeignView
from .params import WordStudyParamsViewABC, WordStudyParamsViewModelABC
from .params.state import WordParamsSourceData, WordStudyParamsViewModel
from .params.view import WordStudyParamsView
from .study import StudyForeignViewABC, WordPresentationViewModelABC
from .study.state import WordPresentationViewModel
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
        binder.bind(WordPresentationViewModelABC, to=WordPresentationViewModel)
        binder.bind(StudyForeignViewABC, to=StudyForeignView)

        # Word study params
        # State data
        binder.bind(WordParamsSourceData, scope=SingletonScope)
        # ViewModel
        binder.bind(WordStudyParamsViewModelABC, to=WordStudyParamsViewModel)
        # View
        binder.bind(WordStudyParamsViewABC, to=WordStudyParamsView)
