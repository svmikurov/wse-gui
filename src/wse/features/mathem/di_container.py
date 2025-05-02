"""Defines dependency injection containers for Mathematical package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features import mathem
from wse.features.mathem.exercises.di_container import (
    MathematicalExercisesContainer,
)


class MathematicalContainer(containers.DeclarativeContainer):
    """Mathematical page container."""

    # Container dependencies
    exercise_container = providers.Container(
        MathematicalExercisesContainer,
    )
    share_container = providers.DependenciesContainer()

    # Mathematical page
    mathematical_model = providers.Factory(
        mathem.MathematicalModel,
    )
    mathematical_view = providers.Factory(
        mathem.MathematicalView,
        content_box=share_container.simple_content,
    )
    mathematical_controller = providers.Factory(
        mathem.MathematicalController,
        model=mathematical_model,
        view=mathematical_view,
    )

    # Multiplication page
    multiplication_model = providers.Factory(
        mathem.MultiplicationModel,
        exercise=exercise_container.multiplication,
        _answer_checker=exercise_container.strict_checker,
        _subject=share_container.subject,
        display_question=share_container.display_model,
        display_answer=share_container.display_model,
        _context=share_container.context,
    )
    multiplication_view = providers.Factory(
        mathem.MultiplicationView,
        _content=share_container.simple_content,
        display_question=share_container.line_display,
        display_answer=share_container.line_display,
        keypad=share_container.digit_keypad,
        _style_config=share_container.style_config,
        _button_factory=share_container.button_factory,
        button_handler=share_container.button_handler,
    )
    multiplication_controller = providers.Factory(
        mathem.MultiplicationController,
        model=multiplication_model,
        view=multiplication_view,
    )

    routes = providers.Dict(
        {
            NavigationID.MATHEMATICAL: mathematical_controller,
            NavigationID.MULTIPLICATION: multiplication_controller,
        }
    )
