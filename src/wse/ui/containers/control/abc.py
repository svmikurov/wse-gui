"""Abstract base class for Exercise control container."""

from abc import ABC
from typing import Literal

from wse.core.base.enums import BaseEnum
from wse.feature.observer.generic import (
    HandleObserverGenABC,
    ObserverManagerGenABC,
)
from wse.ui.base.container import ContainerABC, StyleABC
from wse.ui.base.content import ContentABC, GetContentABC
from wse.utils.i18n import I18N

ControlNotifyT = Literal['handle']


class Action(BaseEnum):
    """Exercise action enumeration."""

    PAUSE = I18N.EXERCISE('Pause')
    NEXT = I18N.EXERCISE('Next')
    KNOWN = I18N.EXERCISE('Known')
    UNKNOWN = I18N.EXERCISE('Unknown')


class ControlContainerABC(
    ObserverManagerGenABC[HandleObserverGenABC[Action]],
    # NotifyGenABC[ControlNotifyT],
    ContainerABC,
    GetContentABC,
    StyleABC,
    ABC,
):
    """ABC for Exercise control container."""

    _content: ContentABC

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._populate_content()
        self._apply_styles()
