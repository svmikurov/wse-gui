"""Application menu mixin."""

import toga

from wse.pages.handlers.goto_handler import set_window_content


class MenuMixin:
    """Application menu mixin."""

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
        """Move to pages box."""
        await set_window_content(self.page_main, box)

    async def goto_main(self, _: toga.Widget, **kwargs: object) -> None:
        """Goto main box, command handler."""
        await self.move_to_page(self.page_main)

    async def goto_glossary(self, _: toga.Widget, **kwargs: object) -> None:
        """Goto glossary box, command handler."""
        await self.move_to_page(self.box_glossary_main)

    async def goto_foreign(self, _: toga.Widget, **kwargs: object) -> None:
        """Goto foreign box, command handler."""
        await self.move_to_page(self.box_foreign_main)
