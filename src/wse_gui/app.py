"""Application for educational exercises on various subjects."""

import toga


class WSEGUI(toga.App):
    """Application."""

    def startup(self) -> None:
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main() -> None:
    """Run application."""
    return WSEGUI()
