"""Test widgets of foreign exercise params page box."""

from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from _pytest.fixtures import FixtureRequest
from _pytest.monkeypatch import MonkeyPatch

from tests.utils import run_until_complete
from wse.app import WSE
from wse.pages import ParamsForeignPage, ParamsGlossaryPage
from wse.widgets.selection import BaseSelection


def set_window_content(
    wse: WSE,
    box: ParamsForeignPage | ParamsGlossaryPage,
) -> None:
    """Assign the box with widgets to window content."""
    wse.main_window.content = box


@pytest.fixture
def box_foreign(wse: WSE) -> ParamsForeignPage:
    """Return the instance of ParamsForeignPage, fixture."""
    box = wse.box_foreign_params
    return box


@pytest.fixture
def box_glossary(wse: WSE) -> ParamsGlossaryPage:
    """Return the instance of ParamsGlossaryPage, fixture."""
    box = wse.box_glossary_params
    return box


@pytest.fixture(params=['box_foreign', 'box_glossary'])
def box(request: FixtureRequest) -> ParamsForeignPage | ParamsGlossaryPage:
    """Return the box fixtures one by one."""
    return request.getfixturevalue(request.param)


def test_foreign_widget_order(
    wse: WSE,
    box_foreign: ParamsForeignPage,
) -> None:
    """Test the widget and containers orger at params page."""
    box = box_foreign
    set_window_content(wse, box)

    assert box.children == [
        box.label_title,
        box.box_params,
        box.btn_goto_exercise,
        box.btn_save_params,
        box.btn_goto_foreign_main,
    ]

    assert box.box_params.children == [
        box.box_selection_order,
        box.box_selection_start,
        box.box_selection_end,
        box.box_selection_category,
        box.box_selection_progress,
        box.box_input_first,
        box.box_input_last,
    ]

    # Selection widgets are parent box-container attr to flex layout.
    assert box.box_selection_start.children == [
        box.label_start.parent,
        box.selection_start_period.parent,
    ]
    assert box.box_selection_end.children == [
        box.label_end.parent,
        box.selection_end_period.parent,
    ]
    assert box.box_selection_category.children == [
        box.label_category.parent,
        box.selection_category.parent,
    ]
    assert box.box_selection_progress.children == [
        box.label_progres.parent,
        box.selection_progress.parent,
    ]
    assert box.box_input_first.children == [
        box.switch_count_first.parent,
        box.input_count_first.parent,
    ]
    assert box.box_input_last.children == [
        box.switch_count_last.parent,
        box.input_count_last.parent,
    ]


def test_glossary_widget_order(
    wse: WSE,
    box_glossary: ParamsGlossaryPage,
) -> None:
    """Test the widget and containers orger at params page."""
    box = box_glossary
    set_window_content(wse, box)

    assert box.children == [
        box.label_title,
        box.box_params,
        box.btn_goto_exercise,
        box.btn_save_params,
        box.btn_goto_glossary_main,
    ]

    assert box.box_params.children == [
        box.box_selection_start,
        box.box_selection_end,
        box.box_selection_category,
        box.box_selection_progress,
        box.box_input_first,
        box.box_input_last,
    ]

    # Selection widgets are included in the parent box to flex layout.
    assert box.box_selection_start.children == [
        box.label_start.parent,
        box.selection_start_period.parent,
    ]
    assert box.box_selection_end.children == [
        box.label_end.parent,
        box.selection_end_period.parent,
    ]
    assert box.box_selection_category.children == [
        box.label_category.parent,
        box.selection_category.parent,
    ]
    assert box.box_selection_progress.children == [
        box.label_progres.parent,
        box.selection_progress.parent,
    ]
    assert box.box_input_first.children == [
        box.switch_count_first.parent,
        box.input_count_first.parent,
    ]
    assert box.box_input_last.children == [
        box.switch_count_last.parent,
        box.input_count_last.parent,
    ]


@pytest.mark.parametrize(
    'box_name, label_text',
    [
        ('box_foreign_params', 'Параметры изучения слов'),
        ('box_glossary_params', 'Параметры изучения терминов'),
    ],
)
def test_label_title(box_name: str, label_text: str, wse: WSE) -> None:
    """Test the label title.

    Testing:
     * ParamsForeignPage and ParamsGlossaryPage classes;
     * that label has a specific text.

    """
    box: ParamsForeignPage | ParamsGlossaryPage = getattr(wse, box_name)

    # The label has a specific text.
    assert box.label_title.text == label_text


@pytest.mark.parametrize(
    'label_name, label_text',
    [
        ('label_start', 'Начало периода:'),
        ('label_end', 'Конец периода:'),
        ('label_category', 'Категория:'),
        ('label_progres', 'Стадия изучения:'),
    ],
)
def test_selections(
    label_name: str,
    label_text: str,
    box: ParamsForeignPage | ParamsGlossaryPage,
) -> None:
    """Test the selection widgets.

    Testing:
     * ParamsForeignPage and ParamsGlossaryPage classes;
     * test that label of selection has specific text.

    """
    label = getattr(box, label_name)

    # Label of selection has specific text.
    assert label.text == label_text


@pytest.mark.parametrize(
    'switch_name, switch_text',
    [
        ('switch_count_first', 'Первые'),
        ('switch_count_last', 'Последние'),
    ],
)
def test_switches(
    switch_name: str,
    switch_text: str,
    box: ParamsForeignPage | ParamsGlossaryPage,
) -> None:
    """Test the switch widgets.

    Testing:
     * ParamsForeignPage and ParamsGlossaryPage classes;
     * test that switch has specific text.

    """
    switch = getattr(box, switch_name)

    # Switch has specific text.
    assert switch.text == switch_text


def test_switch_toggles(box: ParamsForeignPage | ParamsGlossaryPage) -> None:
    """Test the switching.

    Test the switches to add item count (number input) to exercise
    params.

    Testing:
     * ParamsForeignPage and ParamsGlossaryPage classes;
     * test that switch is off by default;
     * test that toggle of first switch to set True;
     * test that toggle of last switch to set True;
     * test that toggle of last switch to set False.

    """
    # A switch is off by default.
    assert not box.switch_count_first.value
    assert not box.switch_count_last.value

    # Toggle the first switch to set True.
    box.switch_count_first.toggle()
    assert box.switch_count_first.value
    assert not box.switch_count_last.value

    # Toggle the last switch to True.
    box.switch_count_last.toggle()
    assert not box.switch_count_first.value
    assert box.switch_count_last.value

    # Toggle the last switch to set False.
    box.switch_count_last.toggle()
    assert not box.switch_count_first.value
    assert not box.switch_count_last.value


@pytest.mark.parametrize(
    'input_name',
    [
        ('input_count_first'),
        ('input_count_last'),
    ],
)
def test_number_inputs(
    input_name: str,
    box: ParamsForeignPage | ParamsGlossaryPage,
) -> None:
    """Test a number input widgets.

    Testing:
     * ParamsForeignPage and ParamsGlossaryPage classes;
     * that a number input has not initial value;
     * that a number input has an increment/decrement step of ten;
     * that a number input has a minimal value.

    """
    switch = getattr(box, input_name)

    # A number input has not initial value.
    assert switch.value is None

    # A number input has an increment/decrement step of ten.
    assert switch.step == 10

    # A number input has a minimal value.
    assert switch.min == 0


@pytest.mark.parametrize(
    'box_name, box_togo',
    [
        ('box_foreign_params', 'box_foreign_exercise'),
        ('box_glossary_params', 'box_glossary_exercise'),
    ],
)
@patch('wse.container.exercise.ExerciseBox.loop_task', new_callable=AsyncMock)
def test_btn_goto_exercise(
    loop_task: AsyncMock,
    box_name: str,
    box_togo: str,
    wse: WSE,
    monkeypatch: MonkeyPatch,
) -> None:
    """Test the button to go to foreign exercise.

    Testing:
     * ParamsForeignPage and ParamsGlossaryPage classes;
     * that button has specific text;
     * that loop task of exercise was awaited;
     * that window content has been refreshed.

    Mocking:
     * get values from param selection widgets;
     * loop task of exercise.

    .. todo::

       Foreign params:
        * add test exercise_box.clean_text_panel()
        * add test exercise_box.task.status = None
    """
    box_params = getattr(wse, box_name)
    box_exercise = getattr(wse, box_togo)
    btn = box_params.btn_goto_exercise

    # Set the test box in the content window.
    set_window_content(wse, box_params)

    # Mock the get param value from widgets, otherwise test failed.
    monkeypatch.setattr(BaseSelection, 'get_alias', Mock(return_value=dict()))

    # Simulate a button press.
    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    # Button has specific text.
    assert btn.text == 'Начать упражнение'

    # The loop task of exercise was awaited.
    loop_task.assert_awaited()

    # The window content has been refreshed.
    assert wse.main_window.content == box_exercise


def test_btn_save_params(
    wse: WSE,
    box: ParamsForeignPage | ParamsGlossaryPage,
    monkeypatch: MonkeyPatch,
) -> None:
    """Test the save params button.

    Testing:
     * ParamsForeignPage and ParamsGlossaryPage classes;
     * that button has specific text;
     * that window content has not been refreshed.

    .. todo::

       Foreign params:
        * add test self.request_put_async(url, payload)

       Glossary params:
        * add test request_post(url, payload)

        * add test the call the functions in button handler.

    """
    btn = box.btn_save_params
    set_window_content(wse, box)

    # Mock the getting param value from widgets,
    # otherwise AttributeError.
    monkeypatch.setattr(BaseSelection, 'get_alias', Mock(return_value=dict()))

    # Simulate a button press.
    btn._impl.simulate_press()

    # Button has specific text.
    assert btn.text == 'Сохранить настройки'

    # The window content has not been refreshed.
    assert wse.main_window.content == box


@pytest.mark.parametrize(
    'box_name, box_togo, btn_name, btn_text',
    [
        (
            'box_foreign_params',
            'box_foreign_main',
            'btn_goto_foreign_main',
            'Иностранный',
        ),
        (
            'box_glossary_params',
            'box_glossary_main',
            'btn_goto_glossary_main',
            'Глоссарий',
        ),
    ],
)
@patch.object(BaseSelection, 'get_alias', return_value=dict())
@patch('httpx.AsyncClient')
def test_btn_goto_sub_main(
    client: MagicMock,
    get_alias: MagicMock,
    box_name: str,
    box_togo: str,
    btn_name: str,
    btn_text: str,
    wse: WSE,
) -> None:
    """Test button to go to sub main page box.

    Test a go to foreign main and glossary main box-containers.

    Testing:
     * ParamsForeignPage and ParamsGlossaryPage classes;
     * that button has specific text;
     * that window content has not been refreshed.

     Mock:
      * ``get_alias`` method of ``BaseSelection`` class,
        otherwise AttributeError;
      * ``httpx.AsyncClient``, otherwise ConnectError.
    """
    box: ParamsForeignPage | ParamsGlossaryPage = getattr(wse, box_name)
    box_next = getattr(wse, box_togo)
    btn = getattr(box, btn_name)

    # Set the test box in the content window.
    set_window_content(wse, box)

    # Simulate a button press.
    btn._impl.simulate_press()

    # Run a fake main loop.
    run_until_complete(wse)

    # The button has a specific text.
    assert btn.text == btn_text

    # The window content has not been refreshed.
    assert wse.main_window.content == box_next
