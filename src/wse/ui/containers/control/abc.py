"""Abstract base class for Exercise control container."""

from abc import ABC, abstractmethod
from typing import Literal, TypeAlias

from wse.core.base.enums import BaseEnum
from wse.feature.observer import generic
from wse.ui.base import container, content
from wse.utils.i18n import I18N

ControlNotifyT = Literal['handle']
HandleObserver: TypeAlias = generic.HandleObserverGenABC['Action']


# TODO: Set new action name for 'OK' action
# The action displays the next phase.
class Action(BaseEnum):
    """Exercise action enumeration."""

    PAUSE = I18N.EXERCISE('Pause')
    UNPAUSE = I18N.EXERCISE('Unpause')
    DISPLAY = I18N.EXERCISE('Display')
    NEXT = I18N.EXERCISE('Next case')
    KNOWN = I18N.EXERCISE('Known')
    UNKNOWN = I18N.EXERCISE('Unknown')


class ControlContainerABC(
    generic.ObserverManagerGenABC[HandleObserver],
    content.GetContentABC,
    container.ContainerABC,
    container.StyleABC,
    ABC,
):
    """ABC for Exercise control container."""

    _content: content.ContentABC

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._populate_content()
        self._apply_styles()

    @abstractmethod
    def update_pause_state(self, pause: bool) -> None:
        """Update pause state."""

    @abstractmethod
    def update_unknown_state(self, enabled: bool) -> None:
        """Update unknown state."""
