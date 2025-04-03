"""WSE application."""

from typing import TypeVar

import toga
from toga.sources import Listener, Source

from wse import controllers, pages
from wse.constants import SCREEN_SIZE
from wse.factory import mvc_factory
from wse.features.shared.base import BaseBox
from wse.menu import MenuMixin
from wse.models.user import User
from wse.pages import ExplorerLayout
from wse.pages.examples.fraction import FractionPage
from wse.pages.examples.main import ExampleLayout
from wse.pages.examples.table_source import TableSourceLayout
from wse.sources.text_panel_main import SourceMainPanel

ModelT = TypeVar('ModelT', bound=Source)
ViewT = TypeVar('ViewT', bound=toga.Box)
ContrT = TypeVar('ContrT', bound=Listener)


class WSE(MenuMixin, toga.App):
    """WSE application."""

    user: ModelT
    source_main_panel: ModelT
    page_home: ViewT
    contr_main: ContrT

    def startup(self) -> None:
        """Construct and show the application."""
        # Models
        self.user = User()
        self.source_main_panel = SourceMainPanel(self.user)

        # Construct MVC
        mvc_factory.initialize(self)

        # TODO: Refactor MVC.
        self.add_controllers()
        self.add_pages()
        self.add_menu()

        # Application start with Main pages box content.
        self.main_window = toga.MainWindow(
            title=self.formal_name,
            size=toga.Size(*SCREEN_SIZE),
        )
        self._override_home_page()
        self.main_window.content = self.page_home.content
        self.main_window.show()

    def _override_home_page(self) -> None:
        from wse.features.home.controller import HomeController
        from wse.features.home.view import HomeView

        screen_content = BaseBox()
        self.page_home = HomeView(screen_content)
        self.contr_main = HomeController(self.page_home)

    ####################################################################
    # Controllers

    def add_controllers(self) -> None:
        """Add controllers."""
        # fmt: off
        self.plc_params_foreign = controllers.ControllerParams()
        self.plc_params_glossary = controllers.ControllerParams()
        self.plc_exercise_foreign = controllers.ControllerExercise(self, self.plc_params_foreign)  # noqa: E501
        self.plc_test_foreign = controllers.ControllerTest()
        self.plc_exercise_glossary = controllers.ControllerExercise(self, self.plc_params_glossary)  # noqa: E501
        self.plc_selected_foreign = controllers.ControllerTable(self.plc_params_foreign)  # noqa: E501
        self.plc_selected_glossary = controllers.ControllerTable(self.plc_params_glossary)  # noqa: E501
        self.plc_form_foreign = controllers.WordFormController()
        self.plc_form_glossary = controllers.TermFormController()
        # fmt: on

    ####################################################################
    # Pages

    def add_pages(self) -> None:
        """Add pages boxes."""
        # fmt: off
        self.box_login = pages.LoginBox(self.user)

        # Temp pages
        self.box_explorer = ExplorerLayout()
        self.box_examples = ExampleLayout()
        self.box_table_source = TableSourceLayout()
        self.box_fraction = FractionPage()

        # Foreign language study pages boxes
        self.box_foreign_main = pages.MainForeignPage()
        self.box_foreign_params = pages.ParamsForeignPage(self.plc_params_foreign)  # noqa: E501
        self.box_foreign_exercise = pages.ExerciseForeignPage(self.plc_exercise_foreign)  # noqa: E501
        self.box_foreign_create = pages.CreateWordPage(self.plc_form_foreign)
        self.box_foreign_update = pages.UpdateWordPage(self.plc_form_foreign)
        self.box_foreign_selected = pages.TableWordPage(self.plc_selected_foreign)  # noqa: E501
        self.box_foreign_tasks = pages.TasksForeignPage()

        # Glossary study pages boxes
        self.box_glossary_main = pages.MainGlossaryWidget()
        self.box_glossary_params = pages.ParamsGlossaryPage(self.plc_params_glossary)  # noqa: E501
        self.box_glossary_exercise = pages.ExerciseGlossaryPage(self.plc_exercise_glossary)  # noqa: E501
        self.box_glossary_create = pages.CreateTermPage(self.plc_form_glossary)
        self.box_glossary_update = pages.UpdateTermPage(self.plc_form_glossary)
        self.box_glossary_selected = pages.TableTermPage(self.plc_selected_glossary)  # noqa: E501

        # Mathematical study pages boxes
        self.box_mathematics_main = pages.MathematicsMainPage()
        self.box_fraction_exercise = pages.FractionExercisePage()

        # Mentoring pages
        self.box_mentoring = pages.MentoringPage()
        self.box_word_test = pages.WordTestPage(self.plc_test_foreign)

        # Listeners of events
        self.plc_exercise_foreign.event.add_listener(self.box_foreign_exercise)
        self.plc_exercise_glossary.event.add_listener(self.box_glossary_exercise)  # noqa: E501
        # fmt: on


def main() -> WSE:
    """Return the app instance."""
    return WSE()
