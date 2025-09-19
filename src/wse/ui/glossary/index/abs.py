"""Abstract base classes for Index Glossary discipline screen."""

from abc import ABC, abstractmethod

from wse.ui.base.abc.navigate import CreateNavButtonABC, NavigateABC
from wse.ui.base.abc.utils import OnCloseABC
from wse.ui.base.abc.view import ViewABC


class IndexGlossaryViewModelABC(
    NavigateABC,
    ABC,
):
    """ABC for Index Glossary screen ViewModel."""

    @abstractmethod
    def refresh_content(self) -> None:
        """Refresh screen context."""


class IndexGlossaryViewABC(
    CreateNavButtonABC,
    OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Index Glossary screen View."""
