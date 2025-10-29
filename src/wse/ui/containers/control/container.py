"""Exercise control container."""

from dataclasses import dataclass

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.ui.base.content.mixins import GetContentMixin
from wse.utils.i18n import I18N

from . import ControlContainerABC


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
        self._btn_next = toga.Button(I18N.EXERCISE('Next'))
        self._btn_pause = toga.Button(I18N.EXERCISE('Pause'))
        self._btn_known = toga.Button(I18N.EXERCISE('Known'))
        self._btn_unknown = toga.Button(I18N.EXERCISE('Unknown'))

    def _update_style(self, config: StyleConfig | ThemeConfig) -> None:
        style = config.control
        self.content.style.update(**style.outbox)
        self._btn_next.style.update(**style.right_btn)
        self._btn_pause.style.update(**style.left_btn)
        self._btn_known.style.update(**style.left_btn)
        self._btn_unknown.style.update(**style.right_btn)
