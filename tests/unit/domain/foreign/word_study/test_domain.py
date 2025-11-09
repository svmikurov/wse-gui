"""Unit tests of Presentation domain."""

import asyncio
from unittest.mock import AsyncMock, Mock, patch

import pytest

from wse.domain.presentation import Presentation


class TestPresentationControl:
    """Test the Presentation control."""

    @pytest.mark.asyncio
    async def test_pause_and_unpause(
        self,
        presentation: Presentation,
    ) -> None:
        """Test the pause/unpause Presentation."""
        # Default on pause
        assert not presentation._unpause_event.is_set()

        presentation.unpause()
        assert presentation._unpause_event.is_set()

        presentation.pause()
        assert not presentation._unpause_event.is_set()

    @pytest.mark.asyncio
    async def test_start(
        self,
        presentation: Presentation,
    ) -> None:
        """Test the start Presentation."""
        presentation.start()

        assert presentation._start_case_event.is_set()
        assert presentation._unpause_event.is_set()

    @pytest.mark.asyncio
    async def test_start_event_call(
        self,
        mock_presentation_domain: Presentation,
        mock_unpause_event: AsyncMock,
        mock_start_case_event: AsyncMock,
    ) -> None:
        """Test the start Presentation event call."""
        mock_presentation_domain.start()

        mock_unpause_event.set.assert_called_once()
        mock_start_case_event.set.assert_called_once()


class TestPresentationLoop:
    """Test the Presentation loop."""

    @pytest.mark.asyncio
    async def test_trigger_definition(
        self,
        mock_presentation_domain: Presentation,
        mock_definition_event: AsyncMock,
    ) -> None:
        """Test the definition trigger of Presentation loop."""
        with patch('wse.domain.presentation.Presentation._wait_timeout'):
            await mock_presentation_domain._trigger_event(
                mock_presentation_domain._definition_event
            )

            mock_definition_event.set.assert_called_once()
            mock_definition_event.clear.assert_called_once()

    @pytest.mark.asyncio
    async def test_trigger_explanation(
        self,
        mock_presentation_domain: Presentation,
        mock_explanation_event: AsyncMock,
    ) -> None:
        """Test the explanation trigger of Presentation loop."""
        with patch('wse.domain.presentation.Presentation._wait_timeout'):
            await mock_presentation_domain._trigger_event(
                mock_presentation_domain._explanation_event
            )

            mock_explanation_event.set.assert_called_once()
            mock_explanation_event.clear.assert_called_once()

    @pytest.mark.asyncio
    async def test_trigger_end_case(
        self,
        mock_presentation_domain: Presentation,
        mock_end_case_event: AsyncMock,
    ) -> None:
        """Test the end case trigger of Presentation loop."""
        with patch('wse.domain.presentation.Presentation._wait_timeout'):
            await mock_presentation_domain._trigger_event(
                mock_presentation_domain._end_case_event
            )

            mock_end_case_event.set.assert_called_once()
            mock_end_case_event.clear.assert_called_once()


class TestStartPresentation:
    """Test start the Presentation domain."""

    @pytest.mark.asyncio
    async def test_start_presentation(
        self,
        presentation: Presentation,
    ) -> None:
        """Test start the Presentation domain."""
        presentation.start()

        assert presentation._start_case_event.is_set()

        # Assert that start case event wait
        try:
            await asyncio.wait_for(
                presentation.wait_start_case_event(), timeout=0.1
            )
        except asyncio.TimeoutError:
            pytest.fail('Wait start case event test failed')

    @pytest.mark.asyncio
    async def test_wait_case_event_on_default(
        self,
        presentation: Presentation,
    ) -> None:
        """Test wait_start_case_event when event is not set."""
        assert not presentation._start_case_event.is_set()

        with pytest.raises(asyncio.TimeoutError):
            await asyncio.wait_for(
                presentation.wait_start_case_event(), timeout=0.1
            )


class TestPresentationInstantiating:
    """Test Presentation domain instantiating."""

    def test_instantiating(self) -> None:
        """Test Presentation domain instantiating."""
        try:
            Presentation(
                start_case_event=Mock(),
                definition_event=Mock(),
                explanation_event=Mock(),
                end_case_event=Mock(),
                unpause_event=Mock(),
                progress_queue=Mock(),
            )
        except Exception:
            pytest.fail('Test Presentation domain instantiating error')
