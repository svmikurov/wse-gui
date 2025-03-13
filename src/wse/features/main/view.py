"""Defines the main screen view."""

import toga

from wse.config.config import Languages
from wse.core.logger import setup_logger
from wse.core.navigation.routes import Routes
from wse.features.shared.observer import Subject
from wse.features.shared.ui.box import ColumnFlexBox
from wse.features.shared.ui.button import ButtonStyled
from wse.features.shared.ui.heading import Heading
from wse.features.shared.ui.text import MultilineInfoPanel
from wse.interfaces.icore import II18NService

logger = setup_logger('features.auth.HomeView')


class HomeView(ColumnFlexBox, Subject):
    """Represents the home screen."""

    def __init__(self, i18n_service: II18NService) -> None:
        """Construct the view."""
        super().__init__()
        Subject.__init__(self)
        # Initializing the translation service
        self.i18n = i18n_service
        self.i18n.add_listener(self)  # Subscribe to change language
        self._ = self.i18n.gettext  # Abbreviation for translation method

        # Creating interface components
        self._create_ui()
        self._add_ui_to_view()
        self.update_ui_texts()  # Initial installation of texts

    def _create_ui(self) -> None:
        self.heading = Heading()
        self.info_panel = MultilineInfoPanel()
        self.exercise_button = ButtonStyled(on_press=self._on_exercises_click)
        self.language_button = ButtonStyled(on_press=self._on_switch_language)

    def _add_ui_to_view(self) -> None:
        self.add(
            self.heading,
            self.info_panel,
            self.exercise_button,
            self.language_button,
        )

    def update_ui_texts(self) -> None:
        """Update all UI elements with current translations."""
        self.heading.text = self._('Home')
        self.exercise_button.text = self._('Exercises')
        self.language_button.text = self._('Switch Language')

    ####################################################################
    # Widget handlers

    def _on_exercises_click(self, _: toga.Widget) -> None:
        self.notify('navigate', route=Routes.EXERCISES)

    def _on_switch_language(self, _: toga.Widget) -> None:
        current_lang = self.i18n.get_current_language()
        if current_lang == Languages.EN:
            new_lang = Languages.RU
        else:
            new_lang = Languages.EN
        self.i18n.change_language(new_lang)
