"""Event time control."""

import asyncio

from . import TimerABC

DEFAULT_TIMEOUT = 2


class Timer(TimerABC):
    """Event time control."""

    def __init__(self, timeout: int | None = None) -> None:
        """Construct the time control."""
        self.timer: asyncio.Task[None] | None = None
        self.pause = False
        self.timeout = DEFAULT_TIMEOUT if not timeout else timeout

    async def start(self, timeout: int | None = None) -> None:
        """Start event timer."""
        timeout_ = self.timeout if not timeout else timeout
        self.timer = asyncio.create_task(asyncio.sleep(timeout_))
        await self.timer

    def is_timer(self) -> bool:
        """Is the timer started."""
        return bool(self.timer)

    def cancel(self) -> None:
        """Cancel event timer."""
        if self.is_timer() and isinstance(self.timer, asyncio.Task):
            self.timer.cancel()

    def on_pause(self) -> None:
        """Pause the event."""
        self.pause = True

    def is_pause(self) -> bool:
        """Is the event paused."""
        return self.pause

    def unpause(self) -> None:
        """Unpause the event."""
        self.pause = False
