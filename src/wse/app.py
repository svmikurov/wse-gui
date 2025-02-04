"""WSE application."""

import toga

from wse import contr as plc
from wse import page
from wse.constants import SCREEN_SIZE
from wse.contrib.factory import factory
from wse.page import ExplorerLayout
from wse.page.examples.fraction import FractionPage
from wse.page.examples.main import ExampleLayout
from wse.page.examples.table_source import TableSourceLayout
from wse.page.handlers.goto_handler import set_window_content
from wse.sources.text_panel_main import SourceMainPanel
from wse.sources.user import SourceUser


class WSE(toga.App):
    """WSE application."""

    def startup(self) -> None:
        """Construct and show the application."""
        # App sources
        self.user = SourceUser()
        self.source_main_panel = SourceMainPanel(self.user)

        # Set user data
        self.user.on_start()

        # Construct MVC
        self.factory = factory
        self.factory.initialize(self)

        # TODO: Refactor MVC.
        self.add_controllers()
        self.add_pages()
        self.add_menu()

        # Application start with Main page box content.
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
        """Add contr."""
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
        """Add page boxes."""
        # fmt: off
        self.box_main = page.MainBox(self.user, self.source_main_panel)
        self.box_login = page.LoginBox(self.user)

        # Temp page
        self.box_explorer = ExplorerLayout()
        self.box_examples = ExampleLayout()
        self.box_table_source = TableSourceLayout()
        self.box_fraction = FractionPage()

        # Foreign language study page boxes
        self.box_foreign_main = page.MainForeignPage()
        self.box_foreign_params = page.ParamsForeignPage(self.plc_params_foreign)  # noqa: E501
        self.box_foreign_exercise = page.ExerciseForeignPage(self.plc_exercise_foreign)  # noqa: E501
        self.box_foreign_create = page.CreateWordPage(self.plc_form_foreign)
        self.box_foreign_update = page.UpdateWordPage(self.plc_form_foreign)
        self.box_foreign_selected = page.TableWordPage(self.plc_selected_foreign)  # noqa: E501
        self.box_foreign_tasks = page.TasksForeignPage()

        # Glossary study page boxes
        self.box_glossary_main = page.MainGlossaryWidget()
        self.box_glossary_params = page.ParamsGlossaryPage(self.plc_params_glossary)  # noqa: E501
        self.box_glossary_exercise = page.ExerciseGlossaryPage(self.plc_exercise_glossary)  # noqa: E501
        self.box_glossary_create = page.CreateTermPage(self.plc_form_glossary)
        self.box_glossary_update = page.UpdateTermPage(self.plc_form_glossary)
        self.box_glossary_selected = page.TableTermPage(self.plc_selected_glossary)  # noqa: E501

        # Mathematical study page boxes
        self.box_mathematics_main = page.MathematicalMainPage()
        self.box_fraction_exercise = page.FractionExercisePage()

        # Mentoring page
        self.box_mentoring = page.MentoringPage()
        self.box_word_test = page.WordTestPage(self.plc_test_foreign)

        # Listeners of events
        self.plc_exercise_foreign.event.add_listener(self.box_foreign_exercise)
        self.plc_exercise_glossary.event.add_listener(self.box_glossary_exercise)  # noqa: E501
        # fmt: on

    ####################################################################
    # Menu

    def add_menu(self) -> None:
        """Add menu."""
        self.menu = toga.Group('Menu')

        # Menu commands
        self.cmd_goto_main = toga.Command(
            self.goto_main,
            text='Главная страница',
            group=self.menu,
            order=1,
        )
        self.cmd_goto_foreign = toga.Command(
            self.goto_foreign,
            text='Иностранный словарь',
            group=self.menu,
            order=2,
        )
        self.cmd_goto_glossary = toga.Command(
            self.goto_glossary,
            text='Глоссарий',
            group=self.menu,
            order=3,
        )
        self.commands.add(
            self.cmd_goto_main,
            self.cmd_goto_glossary,
            self.cmd_goto_foreign,
        )

    async def move_to_page(self, box: toga.Box) -> None:
        """Move to page box."""
        await set_window_content(self.box_main, box)

    async def goto_main(self, _: toga.Widget, **kwargs: object) -> None:
        """Goto main box, command handler."""
        await self.move_to_page(self.box_main)

    async def goto_glossary(self, _: toga.Widget, **kwargs: object) -> None:
        """Goto glossary box, command handler."""
        await self.move_to_page(self.box_glossary_main)

    async def goto_foreign(self, _: toga.Widget, **kwargs: object) -> None:
        """Goto foreign box, command handler."""
        await self.move_to_page(self.box_foreign_main)


def main() -> WSE:
    """Return the app instance."""
    return WSE()
