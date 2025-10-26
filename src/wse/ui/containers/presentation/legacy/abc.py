"""Abstract Base Classes for Presentation container."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.data.sources.base import AccessorSourceABC
from wse.data.sources.glossary import TermPresentationListenerABC
from wse.ui.base.container.abc import CreateContentABC
from wse.ui.glossary.study.abc import ChangeObserverABC

NotifyT = Literal['change',]
AccessorT = Literal['case', 'text']


class PresentationContainerStateListenerABC(ABC):
    """ABC for Presentation container state listener."""

    @abstractmethod
    def change(self, accessor: AccessorT, value: object) -> None:
        """Change value by accessor."""


class PresentationContainerStateABC(
    AccessorSourceABC[
        PresentationContainerStateListenerABC,
        AccessorT,
        NotifyT,
    ],
    ABC,
):
    """ABC for Presentation container state source."""


class PresentationContainerABC(
    TermPresentationListenerABC,
    CreateContentABC,
    ChangeObserverABC,
    ABC,
):
    """ABC for Presentation container."""
