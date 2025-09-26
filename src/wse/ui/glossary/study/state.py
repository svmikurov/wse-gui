"""Terms study UI state."""

from dataclasses import dataclass
from typing import Union

from injector import inject

from wse.domain.glossary import TermPresentationUseCaseABC
from wse.feature.observer.mixins import AddObserverAccessorGen
from wse.ui.base.navigate.mixin import NavigateStateMixin
from wse.ui.containers.numpad.interface import NumPadNotifyT

from . import (
    AccessorT,
    ChangeObserverABC,
    NotifyT,
    TermsStudyViewModelABC,
)


@inject
@dataclass
class TermsStudyViewModel(
    NavigateStateMixin,
    AddObserverAccessorGen[
        ChangeObserverABC,
        Union[NotifyT, NumPadNotifyT],
        AccessorT,
    ],
    TermsStudyViewModelABC,
):
    """Terms study ViewModel."""

    _presentation_case: TermPresentationUseCaseABC

    def refresh_context(self) -> None:
        """Refresh UI context."""
        self._presentation_case.get_presentation()
        self.notify('change', accessor='case', value='Hello from case!')

    def notify(
        self,
        notification: Union[NotifyT, NumPadNotifyT],
        accessor: AccessorT,
        **kwargs: object,
    ) -> None:
        """Notify observer about event."""
        self._subject.notify(notification, accessor=accessor, **kwargs)
