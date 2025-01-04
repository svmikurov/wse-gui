"""WSE application."""

import toga
from toga.command import ActionHandler

from wse import pages
from wse.constants import SCREEN_SIZE
from wse.handlers.goto_handler import set_window_content
from wse.pages import ExplorerLayout
from wse.source.text_panel_main import MainPanelSource
from wse.source.user import UserSource
from wse.widgets.box_page import WidgetMixin


class WSE(toga.App):
    """WSE application."""

    def startup(self) -> None:
        """Construct and show the application."""
        # App sources
        self.user = UserSource()
        self.source_main_panel = MainPanelSource(self.user)

        # Set user data
        self.user.on_start()

        # Construct
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
    # Pages

    def add_pages(self):
        """Add pages."""
        self.box_main = pages.MainBox(self.user, self.source_main_panel)
        self.box_login = pages.LoginBox(self.user)
        self.box_explorer = pages.ExplorerLayout()

        # Foreign language study page boxes
        self.box_foreign_main = pages.MainForeignWidget()
        self.box_foreign_params = pages.ParamsForeignPage()
        self.box_foreign_exercise = pages.ExerciseForeignPage()
        self.box_foreign_create = pages.CreateWordPage()
        self.box_foreign_update = pages.UpdateWordPage()
        self.box_foreign_list = pages.ListForeignPage()

        # Glossary study page boxes
        self.box_glossary_main = pages.MainGlossaryWidget()
        self.box_glossary_params = pages.ParamsGlossaryPage()
        self.box_glossary_exercise = pages.ExerciseGlossaryPage()
        self.box_glossary_create = pages.CreateTermPage()
        self.box_glossary_update = pages.UpdateTermPage()
        self.box_glossary_list = pages.ListGlossaryPage()

    ####################################################################
    # Menu

    def add_menu(self):
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

    async def move_to_page(self, box: WidgetMixin) -> None:
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

    ####################################################################
    # Annotations

    # Sources
    user: UserSource
    source_main_panel: MainPanelSource

    # Page boxes
    box_main: pages.MainBox
    box_explorer: ExplorerLayout
    box_login: pages.LoginBox

    # Foreign language study page boxes
    box_foreign_main: pages.MainForeignWidget
    box_foreign_params: pages.ParamsForeignPage
    box_foreign_exercise: pages.ExerciseForeignPage
    box_foreign_create: pages.CreateWordPage
    box_foreign_update: pages.UpdateWordPage
    box_foreign_list: pages.ListForeignPage

    # Glossary study page boxes
    box_glossary_main: pages.MainGlossaryWidget
    box_glossary_params: pages.ParamsGlossaryPage
    box_glossary_exercise: pages.ExerciseGlossaryPage
    box_glossary_create: pages.CreateTermPage
    box_glossary_update: pages.UpdateTermPage
    box_glossary_list: pages.ListGlossaryPage

    # Menu
    menu: toga.Group
    goto_main: ActionHandler
    goto_foreign: ActionHandler
    goto_glossary: ActionHandler
    cmd_goto_main: toga.Command
    cmd_goto_foreign: toga.Command
    cmd_goto_glossary: toga.Command


def main() -> WSE:
    """Return the app instance."""
    return WSE()
