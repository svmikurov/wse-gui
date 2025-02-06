"""Example run async.

python -m example
"""

import asyncio

import toga


class HelloWorld(toga.App):
    """Example."""

    def startup(self) -> None:
        """Start app."""
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        self.loop.call_soon_threadsafe(self.sync_task, 'Hi')

    def sync_task(self, arg: object) -> None:
        """Call sync method."""
        print(f'INFO: running sync task: {arg}')
        asyncio.create_task(self.async_task('from sync task'))

    async def async_task(self, arg: object) -> None:
        """Call async method."""
        print(f'INFO: running async task: {arg}')

    async def on_running(self) -> None:
        """On running."""
        print('INFO: on_running')


def main() -> HelloWorld:
    """Return example instance."""
    return HelloWorld('Async example', 'org.beeware.toga.tutorial')


if __name__ == '__main__':
    main().main_loop()
