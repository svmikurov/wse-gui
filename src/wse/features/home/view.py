"""Home screen the view module."""

from dataclasses import dataclass

import toga

from wse.pages.widgets import MultilineInfoPanel


class Subject:
    def notify(self, notification, btn_text) -> None: pass


def _(text):
    return text


@dataclass
class Route:
    btn_text: str


class Routes:
    FOREIGN_HOME = Route(_('foreign_home'))
    GLOSSARY_HOME = Route(_('glossary_home'))


class HomeView:
    """View of Home screen."""

    def __init__(self, screen: toga.Box | None = None) -> None:
        """Construct the view."""
        self.content = screen or toga.Box()
        self.subject = Subject()
        self._btn_class = toga.Button

        self._assign_ui_text()
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self.info_panel,
            self._btn_foreign,
        )

    def _create_ui(self) -> None:
        self.info_panel = MultilineInfoPanel()
        # Buttons
        self._btn_foreign = self._create_nav_btn()
        self._btn_glossary = self._create_nav_btn()

    def _assign_ui_text(self) -> None:
        """Assign to widget text a current translation."""
        self._btn_foreign.text = Routes.FOREIGN_HOME.btn_text
        self._btn_glossary.text = Routes.GLOSSARY_HOME.btn_text

    ####################################################################
    # Utility methods

    def _create_nav_btn(self) -> toga.Button:
        return self._btn_class(on_press=self._notify_navigator)

    ####################################################################
    # Notifications

    def _notify_navigator(self, btn: toga.Button) -> None:
        btn_text = btn.text
        self.subject.notify('navigate', btn_text=btn_text)
