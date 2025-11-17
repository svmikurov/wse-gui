"""Test Word study View."""

from typing import Any, Type

import pytest

from wse import di
from wse.domain.foreign import ExerciseAccessorT
from wse.ui import containers
from wse.ui.containers import top_bar
from wse.ui.foreign.study import state, view


class TestCreateView:
    """Test create Word study View."""

    @pytest.mark.parametrize(
        'dependency_attr_name, dependency_class',
        [
            ('_top_bar', top_bar.TopBarController),
            ('_presentation_container', containers.PresenterContainer),
            ('_control_container', containers.ControlContainer),
            ('_info_container', containers.InfoContainer),
        ],
    )
    def test_inject_content(
        self,
        dependency_attr_name: str,
        dependency_class: Type[Any],
        word_study_view: view.StudyForeignView,
    ) -> None:
        """Test that view have injected content."""
        # Assert
        dependency = getattr(word_study_view, dependency_attr_name)
        assert isinstance(dependency, dependency_class)

    def test_view_initialise(self) -> None:
        """Test initialize Word study View."""
        injector = di.create_injector()
        assert injector.get(view.StudyForeignView)


class TestInfoContainer:
    """Test Info container dependency of Word study View."""

    def test_update_context(
        self,
        word_study_view: view.StudyForeignView,
    ) -> None:
        """Test update Info container context."""
        # Arrange
        info = state.TextInfo(progress='8')

        # Act
        word_study_view.change('info', info)

        # Assert
        container = word_study_view._info_container
        for accessor, value in info._asdict().items():
            widget = getattr(container, f'_{accessor}')
            assert widget.text == str(value)


class TestPresentationContainer:
    """Test Presentation container dependency of Word study View."""

    @pytest.mark.parametrize(
        'accessor, value',
        [
            ('definition', 'test definition'),
            ('explanation', 'test explanation'),
        ],
    )
    def test_update_connext(
        self,
        accessor: ExerciseAccessorT,
        value: object,
        word_study_view: view.StudyForeignView,
    ) -> None:
        """Test update Presentation container context."""
        # Act
        word_study_view.change(accessor, value)

        # Assert
        container = word_study_view._presentation_container
        widget = getattr(container, f'_{accessor}')
        assert widget.text == value
