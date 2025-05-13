from random import choice

import toga
from toga.constants import COLUMN, ROW
from toga.sources import Source
from toga.style import Pack

from wse.core.navigation.navigation_id import NavID
from wse.features.shared.content import SimpleContent
from wse.features.shared.enums import StyleID
from wse.interfaces.ifeatures.icontent import IContent
from wse.interfaces.iui.ibutton import IButtonHandler

bee_movies = [
    ('The Secret Life of Bees', '2008', '7.3', 'Drama'),
    ('Bee Movie', '2007', '6.1', 'Animation, Adventure, Comedy'),
    ('Bees', '1998', '6.3', 'Horror'),
    ('The Girl Who Swallowed Bees', '2007', '7.5', 'Short'),
    ('Birds Do It, Bees Do It', '1974', '7.3', 'Documentary'),
    ('Bees: A Life for the Queen', '1998', '8.0', 'TV Movie'),
    ('Bees in Paradise', '1944', '5.4', 'Comedy, Musical'),
    ('Keeper of the Bees', '1947', '6.3', 'Drama'),
]


class Movie:
    # A class to wrap individual movies
    def __init__(self, title, year, rating, genre):
        self.year = int(year)
        self.title = title
        self.rating = float(rating)
        self.genre = genre


class MovieSource(Source):
    def __init__(self):
        super().__init__()
        self._movies = []

    def __len__(self):
        return len(self._movies)

    def __getitem__(self, index):
        return self._movies[index]

    def index(self, entry):
        return self._movies.index(entry)

    def add(self, entry):
        movie = Movie(*entry)
        self._movies.append(movie)
        self._movies.sort(key=lambda m: m.year)
        self.notify('insert', index=self._movies.index(movie), item=movie)

    def remove(self, item):
        index = self.index(item)
        self.notify('pre_remove', index=index, item=item)
        del self._movies[index]
        self.notify('remove', index=index, item=item)

    def clear(self):
        self._movies = []
        self.notify('clear')


class GoodMovieSource(Source):
    # A data source that piggy-backs on a MovieSource, but only
    # exposes *good* movies (rating > 7.0)
    def __init__(self, source):
        super().__init__()
        self._source = source
        self._source.add_listener(self)
        self._removals = {}

    # Implement the filtering of the underlying data source
    def _filtered(self):
        return sorted(
            (m for m in self._source._movies if m.rating > 7.0),
            key=lambda m: -m.rating,
        )

    # Methods required by the ListSource interface
    def __len__(self):
        return len(list(self._filtered()))

    def __getitem__(self, index):
        return self._filtered()[index]

    def index(self, entry):
        return self._filtered().index(entry)

    # A listener that passes on all notifications, but only if they apply
    # to the filtered data source
    def insert(self, index, item):
        # If the item exists in the filtered list, propagate the notification
        for i, filtered_item in enumerate(self._filtered()):
            if filtered_item == item:
                # Propagate the insertion, with the position in the
                # *filtered* list.
                self.notify('insert', index=i, item=item)

    def pre_remove(self, index, item):
        # If the item exists in the filtered list, track that it is being
        # removed; but don't propagate the removal notification until it has
        # been removed from the base data source
        for i, filtered_item in enumerate(self._filtered()):
            if filtered_item == item:
                # Track that the object *was* in the data source
                self._removals[item] = i

    def remove(self, index, item):
        # If the removed item previously existed in the filtered data source,
        # propagate the removal notification.
        try:
            i = self._removals.pop(item)
            self.notify('remove', index=i, item=item)
        except KeyError:
            # object wasn't previously in the data source
            pass

    def clear(self):
        self.notify('clear')


class TableSourceView:
    _content: SimpleContent
    button_handler: IButtonHandler

    def __init__(
        self,
        content: SimpleContent,
        style_config: dict,
        button_handler: IButtonHandler,
    ) -> None:
        """Construct the view."""
        self._content = content
        self._style_config = style_config
        self.button_handler = button_handler
        self._content.id = 'Table source example view'

        # Layout
        self._title_label = toga.Label(
            NavID.EXAMPLES_TABLE_SOURCE,
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
            self.outer_box,
            self._back_button,
        )

    def _layout(self) -> None:
        # Label to show which row is currently selected.
        self.label = toga.Label('Ready.')

        # Create two tables with custom data sources; the data source
        # of the second reads from the first.
        # The headings are also in a different order.
        self.table1 = toga.Table(
            headings=['Year', 'Title', 'Rating', 'Genre'],
            data=MovieSource(),
            style=Pack(flex=1),
            on_select=self.on_select_handler,
        )

        self.table2 = toga.Table(
            headings=['Rating', 'Title', 'Year', 'Genre'],
            data=GoodMovieSource(self.table1.data),
            style=Pack(flex=1),
        )

        # Populate the table
        for entry in bee_movies:
            self.table1.data.add(entry)

        tablebox = toga.Box(
            children=[self.table1, self.table2], style=Pack(flex=1)
        )

        # Buttons
        btn_style = Pack(flex=1)
        btn_insert = toga.Button(
            'Insert Row', on_press=self.insert_handler, style=btn_style
        )
        btn_delete = toga.Button(
            'Delete Row', on_press=self.delete_handler, style=btn_style
        )
        btn_clear = toga.Button(
            'Clear Table', on_press=self.clear_handler, style=btn_style
        )
        btn_box = toga.Box(
            children=[btn_insert, btn_delete, btn_clear],
            style=Pack(direction=ROW),
        )

        # Most outer box
        self.outer_box = toga.Box(
            children=[btn_box, tablebox, self.label],
            style=Pack(
                flex=1,
                direction=COLUMN,
                padding=10,
            ),
        )

    # === Utility methods ===

    # Table callback functions
    def on_select_handler(self, widget, **kwargs):
        row = widget.selection
        self.label.text = (
            f'You selected row: {row.title}'
            if row is not None
            else 'No row selected'
        )

    # Button callback functions
    def insert_handler(self, widget, **kwargs):
        self.table1.data.add(choice(bee_movies))

    def delete_handler(self, widget, **kwargs):
        if self.table1.selection:
            self.table1.data.remove(self.table1.selection)
        elif len(self.table1.data) > 0:
            self.table1.data.remove(self.table1.data[0])
        else:
            print('Table is empty!')

    def clear_handler(self, widget, **kwargs):
        self.table1.data.clear()

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self._content
