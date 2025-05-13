"""Dependency Injection (DI) configuration for Mathematical feature."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavID
from wse.features import mathem


class MathematicalPagesContainer(containers.DeclarativeContainer):
    """DI container for mathematical pages."""

    # Container dependencies

    share_container = providers.DependenciesContainer()
    exercises_container = providers.DependenciesContainer()
    subject_container = providers.DependenciesContainer()

    # Mathematical page

    mathematical_model = providers.Factory(
        mathem.MathematicalModel,
        _subject=subject_container.mathematical_subject,
        _exercise_switcher=exercises_container.exercise_switcher,
    )
    mathematical_view = providers.Factory(
        mathem.MathematicalView,
        _button_handler=share_container.button_handler,
        _content=share_container.simple_content,
        _style_config=share_container.style_config,
        _subject=share_container.subject,
    )
    mathematical_controller = providers.Factory(
        mathem.MathematicalController,
        model=mathematical_model,
        view=mathematical_view,
        _subject=share_container.subject,
    )

    # Calculation page

    calculation_model = providers.Factory(
        mathem.CalculationModel,
        # Core exercise dependencies
        exercise_switcher=exercises_container.exercise_switcher,
        storage=exercises_container.task_conditions_storage,
        render=exercises_container.exercise_render,
        checker=exercises_container.answer_checker,
        # UI display components
        _subject=subject_container.calculation_subject,
    )
    calculation_view = providers.Factory(
        mathem.CalculationView,
        display_question=share_container.line_display,
        display_answer=share_container.line_display,
        display_info=share_container.line_display,
        keypad=share_container.digit_keypad,
        _content=share_container.simple_content,
        _style_config=share_container.style_config,
        _button_handler=share_container.button_handler,
    )
    calculation_controller = providers.Factory(
        mathem.CalculationController,
        model=calculation_model,
        keypad_model=share_container.keypad_model,
        view=calculation_view,
        _subject=share_container.subject,
    )

    # Mathematical page routes

    routes = providers.Dict(
        {
            NavID.MATHEMATICAL: mathematical_controller,
            NavID.MATH_CALCULATION: calculation_controller,
        }
    )
    """Navigation routes for Mathematical feature.
    Keys: NavID constants, Values: Controller instances.
    """
