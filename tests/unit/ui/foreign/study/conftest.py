"""Test Word study screen fixtures."""

import pytest
from injector import Injector

from wse import di
from wse.ui.foreign.study.view import StudyForeignView


@pytest.fixture
def injector() -> Injector:
    """Provide dependency injector fixture."""
    return di.create_injector()


@pytest.fixture
def word_study_view(
    injector: Injector,
) -> StudyForeignView:
    """Provide Word study View fixture."""
    return injector.get(StudyForeignView)
