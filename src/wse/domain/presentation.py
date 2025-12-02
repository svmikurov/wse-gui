"""Presentation domain."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, Final, override

from injector import inject

from .abc import PresentationABC

TIMEOUT_DELTA: Final[float] = 0.025
DEFAULT_DEFINITION_TIMEOUT: Final[int] = 5
DEFAULT_EXPLANATION_TIMEOUT: Final[int] = 2


if TYPE_CHECKING:
    from wse.data.dto import foreign as dto


# TODO: Refactor, too many events.
class Presentation(PresentationABC):
    """Presentation domain."""

    @inject
    def __init__(
        self,
        start_case_event: asyncio.Event,
        definition_event: asyncio.Event,
        explanation_event: asyncio.Event,
        end_case_event: asyncio.Event,
        unpause_event: asyncio.Event,
        complete_phase_event: asyncio.Event,
        progress_queue: asyncio.Queue,  # type: ignore[type-arg]
    ) -> None:
        """Construct the domain."""
        self._start_case_event = start_case_event
        self._definition_event = definition_event
        self._explanation_event = explanation_event
        self._end_case_event = end_case_event
        self._unpause_event = unpause_event
        self._complete_phase_event = complete_phase_event
        self._progress_queue: asyncio.Queue[tuple[float, float]] = (
            progress_queue
        )
        self._phase: asyncio.Task[Any] | None = None

        self._definition_timeout: int = DEFAULT_DEFINITION_TIMEOUT
        self._explanation_timeout: int = DEFAULT_EXPLANATION_TIMEOUT

    @override
    def set_timeout(
        self,
        settings: dto.PresentationSettings,
    ) -> None:
        """Set presentation timeouts."""
        if question_timeout := settings.question_timeout:
            self._definition_timeout = question_timeout
        if answer_timeout := settings.answer_timeout:
            self._explanation_timeout = answer_timeout

    # Presentation loop
    # -----------------

    async def _loop_presentation(self) -> None:
        """Loop presentation."""
        while True:
            await self.wait_start_case_event()

            await self._trigger_event(
                self._definition_event,
                self._definition_timeout,
            )
            await self._trigger_event(
                self._explanation_event,
                self._explanation_timeout,
            )
            await self._trigger_event(self._end_case_event)

    # Wait for presentation event
    # ---------------------------

    @override
    async def wait_start_case_event(self) -> None:
        """Wait for start case event."""
        await self._start_case_event.wait()

    @override
    async def wait_definition_event(self) -> None:
        """Wait for definition phase event."""
        await self._definition_event.wait()

    @override
    async def wait_explanation_event(self) -> None:
        """Wait for explanation phase event."""
        await self._explanation_event.wait()

    @override
    async def wait_end_case_event(self) -> None:
        """Wait for end case event."""
        await self._end_case_event.wait()

    # Presentation control
    # --------------------

    @override
    def start(self) -> None:
        """Start presentation event."""
        self.unpause()
        self._start_case_event.set()
        asyncio.create_task(self._loop_presentation())

    @override
    def pause(self) -> None:
        """Pause presentation."""
        self._unpause_event.clear()

    @override
    def unpause(self) -> None:
        """Unpause presentation."""
        self._unpause_event.set()

    @override
    def stop(self) -> None:
        """Stop presentation."""
        self._start_case_event.clear()

        if self._phase is not None and not self._phase.done():
            self._phase.cancel()

    @override
    def complete_phase(self) -> None:
        """Complete the current phase."""
        self._complete_phase_event.set()

    # Presentation progress
    # ---------------------

    async def get_progress(self) -> tuple[float, float]:
        """Get presentation progress value."""
        return await self._progress_queue.get()

    # Utility methods
    # ---------------

    async def _trigger_event(
        self,
        event: asyncio.Event,
        timeout: float | None = None,
    ) -> None:
        """Trigger event."""
        event.set()
        event.clear()
        self._complete_phase_event.clear()

        if timeout is None:
            # Yield control to event loop to allow other tasks to run.
            await asyncio.sleep(0)
        else:
            self._phase = asyncio.create_task(self._wait_timeout(timeout))
            await self._phase

    async def _wait_timeout(
        self,
        timeout: float,
        time_delta: float = TIMEOUT_DELTA,
    ) -> None:
        """Wait for timeout."""
        elapsed = 0.0

        while elapsed < timeout:
            if self._complete_phase_event.is_set():
                break

            await self._unpause_event.wait()

            self._update_progress(timeout, elapsed)

            await asyncio.sleep(time_delta)
            elapsed += time_delta

    def _update_progress(self, max: float, value: float) -> None:
        # Clear out old messages so they don't accumulate.
        while not self._progress_queue.empty():
            self._progress_queue.get_nowait()
        self._progress_queue.put_nowait((max, value))
