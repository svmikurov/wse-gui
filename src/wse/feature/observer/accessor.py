"""Listener mixin via accessors."""

import logging
from dataclasses import dataclass
from typing import Generic

import toga

from wse.types import AccessorT, NotifyT, ObserverT

from .abc import AccessorNotifyGenABC, SubjectABC
from .generic import ObserverManagerGenABC
from .mixins import ObserverManagerGen

log = logging.getLogger(__name__)


class AccessorMixin:
    """Listener via accessors."""

    _accessors: tuple[str, ...]

    def _check_accessors(self) -> None:
        """Check that UI attr name corresponding to accessor."""
        if not self._accessors:
            raise RuntimeError(
                f'Class `{self.__class__.__name__}` must define non-empty '
                f'`_accessors. Got: {self._accessors!r}`'
            )

        for accessor in self._accessors:
            self._has_accessor(f'_{accessor}')

    def _get_ui(self, accessor: str) -> toga.Widget:
        """Get UI via accessor."""
        try:
            return getattr(self, f'_{accessor}')  # type: ignore[no-any-return]

        except AttributeError:
            raise LookupError(
                f"Unknown accessor '{accessor}'. Available: {self._accessors}"
            ) from None

    def _has_accessor(self, accessor: str) -> None:
        if not hasattr(self, accessor):
            raise AttributeError(
                f"Not implemented attribute '{accessor}' in "
                f'`{self.__class__.__name__}` for observer pattern'
            )


@dataclass
class NotifyAccessorGen(Generic[NotifyT, AccessorT]):
    """Notify observer about event."""

    _subject: SubjectABC

    def notify(
        self,
        notification: NotifyT,
        accessor: AccessorT,
        **kwargs: object,
    ) -> None:
        """Notify observer about event."""
        try:
            self._subject.notify(notification, accessor=accessor, **kwargs)
        except Exception:
            log.exception('Accessor notification error')
            raise


class SubjectAccessorGenABC(
    ObserverManagerGenABC[ObserverT],
    AccessorNotifyGenABC[NotifyT, AccessorT],
    Generic[ObserverT, NotifyT, AccessorT],
):
    """ABC for Subject observer with accessor."""


@dataclass
class AddObserverAccessorGen(
    ObserverManagerGen[ObserverT],
    NotifyAccessorGen[NotifyT, AccessorT],
    Generic[ObserverT, NotifyT, AccessorT],
):
    """Mixin that enables observer subscription capability."""
