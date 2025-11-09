"""Foreign word study Locale source tests."""

from unittest.mock import Mock

import pytest

from wse.data.sources.foreign.study import WordStudyLocaleSource


@pytest.fixture
def mock_study_data() -> Mock:
    """Mock the Word study data."""
    return Mock()


@pytest.fixture
def study_locale_source(
    mock_study_data: Mock,
) -> WordStudyLocaleSource:
    """Test the Word study locale source instantiation."""
    return WordStudyLocaleSource(
        data=mock_study_data,
    )
