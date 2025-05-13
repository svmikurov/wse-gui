"""Defines Selection exemple page view."""

import toga
from toga.constants import COLUMN, ROW
from toga.sources import Source
from toga.style import Pack

from wse.core.navigation.navigation_id import NavID
from wse.features.shared.enums import StyleID
from wse.interfaces.ifeatures.icontent import IContent
from wse.interfaces.iui.ibutton import IButtonHandler

# ruff: noqa: ANN001, ANN201, ANN202, D102, D415, E501


CARBON = 'Carbon'
YTTERBIUM = 'Ytterbium'
THULIUM = 'Thulium'
OPTIONS = [CARBON, YTTERBIUM, THULIUM]
DATA_OPTIONS = [
    {'name': CARBON, 'number': 6, 'weight': 12.011},
    {'name': YTTERBIUM, 'number': 70, 'weight': 173.04},
    {'name': THULIUM, 'number': 69, 'weight': 168.93},
]


class Color:
    def __init__(self, name: str, number: int, weight: float) -> None:
        self.name = name
        self.number = number
        self.weight = weight


class ColorSource(Source):
    def __init__(self) -> None:
        super().__init__()
        self._colors = []

    def __getitem__(self, index):
        return self._colors[index]

    def add(self, entry: dict[str, str | int | float]) -> None:
        """Add coloros."""
        color = Color(**entry)
        self._colors.append(color)
        self.notify('insert', index=self._colors.index(color), item=color)

    def clear(self):
        self._colors = []
        self.notify('clear')


class SelectionView:
    """Selection exemple page view."""

    def __init__(
        self,
        content: IContent,
        style_config: dict,
        button_handler: IButtonHandler,
    ) -> None:
        """Construct the view."""
        self._content = content
        self._style_config = style_config
        self.button_handler = button_handler
        self._content.id = 'Selection examples view'

        # Layout
        self._title_label = toga.Label(
            NavID.EXAMPLES_SELECTION,
            style=Pack(**self._style_config.get(StyleID.TITLE)),
        )
        self._back_button = toga.Button(
            'Back',
            style=Pack(**self._style_config.get(StyleID.DEFAULT_BUTTON)),
            on_press=self.button_handler.navigate,
        )

        self._layout()
        self._populate_content()

    def _populate_content(self):
        self.content.add(
            self._title_label,
            *self.ui.children,
            toga.Box(style=Pack(flex=1)),  # Flex stub
            self._back_button,
        )

    # -=== Toga example ===-

    def _layout(self):
        # set up common styles
        label_style = Pack(flex=1, padding_right=24)
        box_style = Pack(direction=ROW, padding=10)

        # Add the content on the main window
        self.selection = toga.Selection(items=OPTIONS)
        self.empty_selection = toga.Selection()
        self.source_selection = toga.Selection(
            accessor='name',
            items=DATA_OPTIONS,
        )
        self.custom_source_selection = toga.Selection(
            accessor='number',
            items=ColorSource(),
            on_change=self.on_change_notify,
        )

        self.ui = toga.Box(
            children=[
                toga.Box(
                    style=box_style,
                    children=[
                        toga.Label('Select an element', style=label_style),
                        self.selection,
                    ],
                ),
                toga.Box(
                    style=box_style,
                    children=[
                        toga.Label('Empty selection', style=label_style),
                        self.empty_selection,
                    ],
                ),
                toga.Box(
                    style=box_style,
                    children=[
                        toga.Label('Selection from source', style=label_style),
                        self.source_selection,
                    ],
                ),
                toga.Box(
                    style=box_style,
                    children=[
                        toga.Label(
                            'Selection from Source',
                            style=label_style,
                        ),
                        toga.Button(
                            'Populate', on_press=self.populate_selection
                        ),
                        self.custom_source_selection,
                    ],
                ),
                toga.Box(
                    style=box_style,
                    children=[
                        toga.Button('Print', on_press=self.report_selection),
                        toga.Button('Carbon', on_press=self.set_carbon),
                        toga.Button('Ytterbium', on_press=self.set_ytterbium),
                        toga.Button('Thulium', on_press=self.set_thulium),
                    ],
                ),
                toga.Box(
                    style=box_style,
                    children=[
                        toga.Label(
                            'on_change callback',
                            style=label_style,
                        ),
                        toga.Selection(
                            on_change=self.my_on_change,
                            items=[
                                'Dubnium',
                                'Holmium',
                                'Zirconium',
                                'Dubnium',
                                'Holmium',
                                'Zirconium',
                            ],
                        ),
                    ],
                ),
                toga.Box(
                    style=box_style,
                    children=[
                        toga.Label(
                            'Long lists should scroll', style=label_style
                        ),
                        toga.Selection(items=dir(toga)),
                    ],
                ),
                toga.Box(
                    style=box_style,
                    children=[
                        toga.Label('Use some style!', style=label_style),
                        toga.Selection(
                            style=Pack(width=200, padding=24),
                            items=['Curium', 'Titanium', 'Copernicium'],
                        ),
                    ],
                ),
                toga.Box(
                    style=box_style,
                    children=[
                        toga.Label('Disabled', style=label_style),
                        toga.Selection(
                            items=[
                                'Helium',
                                'Neon',
                                'Argon',
                                'Krypton',
                                'Xenon',
                                'Radon',
                                'Oganesson',
                            ],
                            enabled=False,
                        ),
                    ],
                ),
            ],
            style=Pack(direction=COLUMN, padding=24),
        )

    def set_carbon(self, widget):
        self.selection.value = CARBON

    def set_ytterbium(self, widget):
        self.selection.value = YTTERBIUM

    def set_thulium(self, widget):
        self.selection.value = THULIUM

    def my_on_change(self, selection):
        # get the current value of the slider with `selection.value`

        print(f'The selection widget changed to {selection.value}')

    def report_selection(self, widget):
        print(
            f'Element: {self.selection.value!r}; '
            f'Empty: {self.empty_selection.value!r}; '
            f'Source: {self.source_selection.value.name} '
            f'has weight {self.source_selection.value.weight}'
        )

    # === Custom ===

    def populate_selection(self, _: toga.Widget) -> None:
        # Updating `items` calls the `on_change` method.
        # Disable the method for the duration of the population.
        self.custom_source_selection.on_change = None
        self.custom_source_selection.items.clear()

        for item in DATA_OPTIONS:
            self.custom_source_selection.items.add(item)

        # Enable the method after population.
        self.custom_source_selection.on_change = self.on_change_notify

    def on_change_notify(self, widget: toga.Widget, *args: object) -> None:
        print('Populated')
        print(f'{widget.value = }')
        print(f'{args = }')

    # === Utility methods ===

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self._content
