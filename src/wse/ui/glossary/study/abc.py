"""Abstract Base Classes for Terms study screen."""

from abc import ABC, abstractmethod
from typing import Literal, Union

from wse.feature.observer.generic import (
    SubjectAccessorGenABC,
    UpdateObserverABC,
)
from wse.ui.base.content.abc import GetContentABC
from wse.ui.base.navigate import NavigateABC
from wse.ui.base.view.abc import ViewABC
from wse.ui.containers.numpad.interface import NumPadNotifyT

NotifyT = Literal['change']
AccessorT = Literal['case', 'text']


class ChangeObserverABC(UpdateObserverABC[AccessorT]):
    """ABC for ..."""


class TermsStudyViewModelABC(
    SubjectAccessorGenABC[
        ChangeObserverABC,
        Union[NotifyT | NumPadNotifyT],
        AccessorT,
    ],
    NavigateABC,
    ABC,
):
    """ABC for Terms study ViewModel."""

    @abstractmethod
    def refresh_context(self) -> None:
        """Refresh UI context."""


class TermsStudyViewABC(
    GetContentABC,
    ViewABC,
    ABC,
):
    """ABC for Terms study View."""
