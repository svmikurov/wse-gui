"""Abstract base classes for Index Glossary discipline screen."""

from abc import ABC, abstractmethod

from wse.feature.base import ViewABC
from wse.feature.base.container import CreateNavButtonABC
from wse.ui.base.abc import CloseScreenABC, NavigateABC


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
    CloseScreenABC,
    ViewABC,
    ABC,
):
    """ABC for Index Glossary screen View."""
