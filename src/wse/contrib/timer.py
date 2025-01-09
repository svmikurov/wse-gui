"""Event time control."""

import asyncio

from toga.sources import Source

from wse.constants import DEFAULT_TIMEOUT


class Timer:
    """Event time control."""

    def __init__(self) -> None:
        """Construct the time control."""
        self.timer = None
        self.pause = False
        self.has_timeout = False
        self.timeout = DEFAULT_TIMEOUT
        # Progress bar
        self.countdown = None
        self.progress_bar_source = Source()  # To add progress bar as listener.

    async def start(self) -> None:
        """Start event timer.

        **DEPRECATED** - After applying the ProgressBar widget.
        """
        self.timer = asyncio.create_task(asyncio.sleep(self.timeout))
        await self.timer

    def is_timer(self) -> bool:
        """Is the timer started.

        **DEPRECATED** - After applying the ProgressBar widget.
        """
        return bool(self.timer)

    def is_countdown(self) -> bool:
        """Is the timer started."""
        return bool(self.countdown)

    def cancel(self) -> None:
        """Cancel event timer."""
        # **DEPRECATED**
        # if self.is_timer():
        #     self.timer.cancel()
        if self.is_countdown():
            self.countdown.cancel()

    def on_pause(self) -> None:
        """Pause the event."""
        self.pause = True

    def is_pause(self) -> bool:
        """Is the event paused."""
        return self.pause

    def unpause(self) -> None:
        """Unpause the event."""
        self.pause = False

    async def start_counter(self) -> None:
        """Notify time progress bar about next step."""
        smooth = 15
        step = 1 / smooth
        self.progress_bar_source.notify('reset')

        for _ in range(self.timeout * smooth):
            self.countdown = asyncio.create_task(asyncio.sleep(step))
            self.progress_bar_source.notify('increase', step_size=step)

            # Break on pause and stop drawing the progress line.
            if self.is_pause():
                break

            # Break on restart.
            if not self.is_countdown():
                break

            await self.countdown
