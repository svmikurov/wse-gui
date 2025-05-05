"""Defines dependency injection containers for Mathematical package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features import mathem
from wse.features.mathem.exercises.di_container import (
    ExercisesContainer,
)


class MathematicalContainer(containers.DeclarativeContainer):
    """Mathematical page container."""

    # Container dependencies
    exercise_container = providers.Container(
        ExercisesContainer,
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

    # Calculation page
    calculation_model = providers.Factory(
        mathem.CalculationModel,
        # Exercise dependencies
        exercise=exercise_container.multiplication_exercise,
        storage=exercise_container.task_conditions_storage,
        render=exercise_container.exercise_render,
        checker=exercise_container.answer_checker,
        # MVC model dependencies
        _subject=share_container.subject,
        display_question=share_container.display_model,
        display_answer=share_container.keypad_model,
        display_info=share_container.display_model,
    )
    calculation_view = providers.Factory(
        mathem.CalculationView,
        _content=share_container.simple_content,
        display_question=share_container.line_display,
        display_answer=share_container.line_display,
        display_info=share_container.line_display,
        keypad=share_container.digit_keypad,
        _style_config=share_container.style_config,
        _button_factory=share_container.button_factory,
        button_handler=share_container.button_handler,
    )
    calculation_controller = providers.Factory(
        mathem.CalculationController,
        _subject=share_container.subject,
        model=calculation_model,
        view=calculation_view,
    )

    routes = providers.Dict(
        {
            NavigationID.MATHEMATICAL: mathematical_controller,
            NavigationID.MATH_CALCULATION: calculation_controller,
        }
    )
