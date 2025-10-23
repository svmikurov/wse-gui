"""Index Foreign discipline ViewModel."""

from dataclasses import dataclass

from injector import inject

from wse.ui.base.navigate.mixin import NavigateStateMixin

from . import IndexForeignViewModelABC


@inject
@dataclass
class IndexForeignViewModel(
    NavigateStateMixin,
    IndexForeignViewModelABC,
):
    """Index Glossary screen ViewModel."""
