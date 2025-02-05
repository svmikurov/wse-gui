"""WSE application."""

import toga

from wse import controllers as plc
from wse import pages
from wse.constants import SCREEN_SIZE
from wse.contrib.factory import mvc_factory
from wse.menu import MenuMixin
from wse.models.user import SourceUser
from wse.pages import ExplorerLayout
from wse.pages.examples.fraction import FractionPage
from wse.pages.examples.main import ExampleLayout
from wse.pages.examples.table_source import TableSourceLayout
from wse.sources.text_panel_main import SourceMainPanel


class WSE(MenuMixin, toga.App):
    """WSE application."""

    def startup(self) -> None:
        """Construct and show the application."""
        # App sources
        self.user = SourceUser()
        self.source_main_panel = SourceMainPanel(self.user)

        # Set user data
        self.user.on_start()

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
        self.main_window.content = self.box_main
        self.box_main.update_widgets()  # by user auth status
        self.main_window.show()

    ####################################################################
    # Controllers

    def add_controllers(self) -> None:
        """Add controllers."""
        # fmt: off
        self.plc_params_foreign = plc.ControllerParams()
        self.plc_params_glossary = plc.ControllerParams()
        self.plc_exercise_foreign = plc.ControllerExercise(self, self.plc_params_foreign)  # noqa: E501
        self.plc_test_foreign = plc.ControllerTest()
        self.plc_exercise_glossary = plc.ControllerExercise(self, self.plc_params_glossary)  # noqa: E501
        self.plc_selected_foreign = plc.ControllerTable(self.plc_params_foreign)  # noqa: E501
        self.plc_selected_glossary = plc.ControllerTable(self.plc_params_glossary)  # noqa: E501
        self.plc_form_foreign = plc.WordFormController()
        self.plc_form_glossary = plc.TermFormController()
        # fmt: on

    ####################################################################
    # Pages

    def add_pages(self) -> None:
        """Add pages boxes."""
        # fmt: off
        self.box_main = pages.MainBox(self.user, self.source_main_panel)
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
        self.box_mathematics_main = pages.MathematicalMainPage()
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
