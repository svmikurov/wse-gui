"""Button handlers to go to specific pages box."""

from collections import deque

import toga

# Visited pages are stored in the history for the "Back" button.
browsing_history = deque(maxlen=10)


async def set_window_content(
    widget: toga.Widget,
    box: toga.Box,
    action: str = 'next',
    **kwargs: object,
) -> None:
    """Set pages box in window content."""
    # Visited last 10 pages are stored in the history,
    # but not the previous ones.
    if action != 'back':
        current_page = widget.app.main_window.content
        browsing_history.append(current_page)

    # Assign another pages to window content.
    widget.app.main_window.content = box

    # Some pages are has specific events when opened.
    try:
        await box.on_open(widget, **kwargs)
    except AttributeError:
        # The pages has no events when opened.
        pass


async def goto_main_handler(widget: toga.Widget) -> None:
    """Go to main, button handler."""
    box = widget.root.app.page_main
    await set_window_content(widget, box)


async def goto_login(widget: toga.Widget) -> None:
    """Go to log in, button handler."""
    box = widget.root.app.box_login
    await set_window_content(widget, box)


async def goto_back_handler(widget: toga.Widget) -> None:
    """Go to previous pages, button handler."""
    previous_page = browsing_history.pop()
    await set_window_content(widget, previous_page, 'back')


########################################################################
# Mentoring


async def goto_mentoring(widget: toga.Widget) -> None:
    """Go to mentoring pages, button handler."""
    box = widget.root.app.box_mentoring
    await set_window_content(widget, box)


async def goto_word_test_handler(widget: toga.Widget) -> None:
    """Go to foreign word test pages, button handler."""
    box = widget.root.app.box_word_test
    await set_window_content(widget, box)


########################################################################
# Foreign


async def goto_foreign_main(widget: toga.Widget) -> None:
    """Go to foreign main, button handler."""
    box = widget.root.app.box_foreign_main
    await set_window_content(widget, box)


async def goto_foreign_create(widget: toga.Widget, **kwargs: object) -> None:
    """Go to foreign create, button handler."""
    box = widget.root.app.box_foreign_create
    await set_window_content(widget, box, **kwargs)


async def goto_foreign_update_handler(
    widget: toga.Widget, **kwargs: object
) -> None:
    """Go to foreign update, button handler."""
    box = widget.root.app.box_foreign_update
    await set_window_content(widget, box, **kwargs)


async def goto_foreign_table_handler(widget: toga.Widget) -> None:
    """Go to foreign list of selected words, button handler."""
    box = widget.root.app.box_foreign_selected
    await set_window_content(widget, box)


async def goto_foreign_params(widget: toga.Widget) -> None:
    """Go to foreign params, button handler."""
    box = widget.root.app.box_foreign_params
    await set_window_content(widget, box)


async def goto_foreign_exercise_handler(widget: toga.Widget) -> None:
    """Go to foreign exercise, button handler."""
    box = widget.root.app.box_foreign_exercise
    await set_window_content(widget, box)


async def goto_foreign_tasks(widget: toga.Widget) -> None:
    """Go to foreign tasks, button handler."""
    box = widget.root.app.box_foreign_tasks
    await set_window_content(widget, box)


async def goto_foreign_test(widget: toga.Widget) -> None:
    """Go to foreign test, button handler."""
    box = widget.root.app.box_word_test
    await set_window_content(widget, box)


########################################################################
# Glossary


async def goto_glossary_main(widget: toga.Widget) -> None:
    """Go to glossary main, button handler."""
    box = widget.root.app.box_glossary_main
    await set_window_content(widget, box)


async def goto_glossary_create(widget: toga.Widget, **kwargs: object) -> None:
    """Go to glossary create, button handler."""
    box = widget.root.app.box_glossary_create
    await set_window_content(widget, box, **kwargs)


async def goto_glossary_update_handler(
    widget: toga.Widget, **kwargs: object
) -> None:
    """Go to glossary update, button handler."""
    box = widget.root.app.box_glossary_update
    await set_window_content(widget, box, **kwargs)


async def goto_glossary_selected_handler(widget: toga.Widget) -> None:
    """Go to glossary list of selected terms, button handler."""
    box = widget.root.app.box_glossary_selected
    await set_window_content(widget, box)


async def goto_glossary_params(widget: toga.Widget) -> None:
    """Go to glossary params, button handler."""
    box = widget.root.app.box_glossary_params
    await set_window_content(widget, box)


async def goto_glossary_exercise_handler(widget: toga.Widget) -> None:
    """Go to glossary exercise, button handler."""
    box = widget.root.app.box_glossary_exercise
    await set_window_content(widget, box)


#########################################################################
# Mathematical


async def goto_math_main(widget: toga.Widget) -> None:
    """Go to mathematics main, button handler."""
    box = widget.root.app.box_mathematics_main
    await set_window_content(widget, box)


async def goto_multiplication_exercise_handler(widget: toga.Widget) -> None:
    """Go to multiplication exercise, button handler."""
    box = widget.root.app.page_mult
    await set_window_content(widget, box)


async def goto_calculations_exercise(widget: toga.Widget) -> None:
    """Go to calculations exercise, button handler."""
    box = widget.root.app.page_calc
    await set_window_content(widget, box)


async def goto_fraction_exercise(widget: toga.Widget) -> None:
    """Go to fraction exercise, button handler."""
    box = widget.root.app.box_fraction_exercise
    await set_window_content(widget, box)


#########################################################################
# Examples


async def goto_explorer(widget: toga.Widget) -> None:
    """Go to explorer pages, button handler."""
    box = widget.root.app.box_explorer
    await set_window_content(widget, box)


async def goto_examples_handler(widget: toga.Widget) -> None:
    """Go to table source pages, button handler."""
    box = widget.root.app.box_examples
    await set_window_content(widget, box)


async def goto_table_source_handler(widget: toga.Widget) -> None:
    """Go to table source pages, button handler."""
    box = widget.root.app.box_table_source
    await set_window_content(widget, box)


async def goto_fraction_handler(widget: toga.Widget) -> None:
    """Go to fraction pages, button handler."""
    box = widget.root.app.box_fraction
    await set_window_content(widget, box)
