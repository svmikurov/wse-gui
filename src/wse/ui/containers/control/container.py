"""Exercise control container."""

from dataclasses import dataclass
from typing import TYPE_CHECKING

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.base.enums import BaseEnum
from wse.ui.base.content.mixins import GetContentMixin
from wse.utils import decorators
from wse.utils.i18n import I18N

from . import ControlContainerABC

if TYPE_CHECKING:
    from toga.widgets.button import OnPressHandler


class Action(BaseEnum):
    """Exercise action enumeration."""

    PAUSE = I18N.EXERCISE('Pause')
    NEXT = I18N.EXERCISE('Next')
    KNOWN = I18N.EXERCISE('Known')
    UNKNOWN = I18N.EXERCISE('Unknown')


@inject
@dataclass
class ControlContainer(
    GetContentMixin,
    ControlContainerABC,
):
    """Exercise control container."""

    def _populate_content(self) -> None:
        self._content.add(
            toga.Box(children=[self._btn_pause, self._btn_next]),
            toga.Box(children=[self._btn_known, self._btn_unknown]),
        )

    def _create_ui(self) -> None:
        self._btn_next = self._create_btn(Action.NEXT)
        self._btn_pause = self._create_btn(Action.PAUSE)
        self._btn_known = self._create_btn(Action.KNOWN)
        self._btn_unknown = self._create_btn(Action.UNKNOWN)

    def _update_style(self, config: StyleConfig | ThemeConfig) -> None:
        style = config.control
        self.content.style.update(**style.outbox)
        self._btn_next.style.update(**style.right_btn)
        self._btn_pause.style.update(**style.left_btn)
        self._btn_known.style.update(**style.left_btn)
        self._btn_unknown.style.update(**style.right_btn)

    def _create_btn(self, text: Action) -> toga.Button:
        return toga.Button(text, on_press=self._on_press)  # type: ignore[arg-type]

    # TODO: Implement method
    @decorators.log_unimplemented_call
    def _on_press(self, button: toga.Button) -> OnPressHandler:  # type: ignore[empty-body]
        """Button callback."""
        pass
