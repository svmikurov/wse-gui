"""Glossary discipline DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from .index import IndexGlossaryViewABC, IndexGlossaryViewModelABC
from .index.state import IndexGlossaryViewModel
from .index.view import IndexGlossaryView
from .terms import TermsViewABC, TermsViewModelABC
from .terms.state import TermsTableSource, TermsViewModel
from .terms.view import TermsView


class GlossaryModule(Module):
    """Glossary discipline DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # Index
        binder.bind(IndexGlossaryViewABC, to=IndexGlossaryView)
        binder.bind(IndexGlossaryViewModelABC, to=IndexGlossaryViewModel)

        # Terms
        binder.bind(TermsTableSource, scope=SingletonScope)
        binder.bind(TermsViewModelABC, to=TermsViewModel)
        binder.bind(TermsViewABC, to=TermsView)
