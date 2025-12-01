"""Foreign discipline DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from .index import IndexForeignViewABC, IndexForeignViewModelABC
from .index.state import IndexForeignViewModel
from .index.view import IndexForeignView
from .params import WordStudyParamsViewABC, WordStudyParamsViewModelABC
from .params.state import WordParametersUIState, WordStudyParamsViewModel
from .params.view import WordStudyParamsView
from .presentation import WordPresentationViewABC, WordPresentationViewModelABC
from .presentation.state import WordPresentationViewModel
from .presentation.view import WordPresentationView


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
        binder.bind(WordPresentationViewABC, to=WordPresentationView)

        # Word study params
        binder.bind(WordParametersUIState, scope=SingletonScope)
        binder.bind(WordStudyParamsViewModelABC, to=WordStudyParamsViewModel)
        binder.bind(WordStudyParamsViewABC, to=WordStudyParamsView)
