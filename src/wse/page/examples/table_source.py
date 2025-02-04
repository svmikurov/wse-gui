"""Table source example."""

from random import choice

import toga
from toga.constants import COLUMN
from toga.sources import Source
from toga.style import Pack
from typing_extensions import Self

from wse.page.handlers.goto_handler import goto_back_handler
from wse.page.widgets.button import BtnApp

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
    """A class to wrap individual movies."""

    def __init__(self, title: str, year: str, rating: str, genre: str) -> None:
        """Construct the movie."""
        self.title = title
        self.year = int(year)
        self.rating = float(rating)
        self.genre = genre


class MovieSource(Source):
    """Source of movie."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._movies: list[Movie] = []

    def __len__(self) -> int:
        """Return len of source."""
        return len(self._movies)

    def __getitem__(self, index: int) -> Movie:
        """Get item by index."""
        return self._movies[index]

    def index(self, entry: Movie) -> int:
        """Return index of item."""
        return self._movies.index(entry)

    #####################################################################
    # Listener methods

    def add(self, entry: Movie) -> None:
        """Add item."""
        movie = Movie(*entry)
        self._movies.append(movie)
        self._movies.sort(key=lambda m: m.year)
        index = self._movies.index(movie)
        self.notify('insert', index=index, item=movie)

    def remove(self, item: Movie) -> None:
        """Remove item."""
        index = self._movies.index(item)
        self.notify('pre_remove', index=index, item=item)
        del self._movies[index]
        self.notify('remove', index=index, item=item)

    def clear(self) -> None:
        """Clear the source."""
        self._movies = []
        self.notify('clear')


class GoodMovieSource(Source):
    """Exposes *good* movies."""

    # A data source that piggy-backs on a MovieSource, but only
    # exposes *good* movies (rating > 7.0)
    def __init__(self, source: MovieSource) -> None:
        """Construct the source."""
        super().__init__()
        self._source = source
        self._source.add_listener(self)
        self._removals = {}

    # Implement the filtering of the underlying data source
    def _filtered(self) -> list:
        """Return filtred list of items."""
        return sorted(
            (m for m in self._source._movies if m.rating > 7.0),
            key=lambda m: -m.rating,
        )

    # Methods required by the ListSource interface
    def __len__(self) -> int:
        """Return len of source."""
        return len(list(self._filtered()))

    def __getitem__(self, index: int) -> Movie:
        """Get item by index."""
        return self._filtered()[index]

    def index(self, entry: Movie) -> int:
        """Return index by item."""
        return self._filtered().index(entry)

    #####################################################################
    # Listener methods

    def add(self, entry: Movie) -> None:
        """Add item."""
        movie = Movie(*entry)
        self._movies.append(movie)
        self._movies.sort(key=lambda m: m.year)
        index = self._movies.index(movie)
        self.notify('insert', index=index, item=movie)

    def remove(self, item: Movie) -> None:
        """Remove item."""
        index = self._movies.index(item)
        self.notify('pre_remove', index=index, item=item)
        del self._movies[index]
        self.notify('remove', index=index, item=item)

    def clear(self) -> None:
        """Clear the source."""
        self._movies = []
        self.notify('clear')

    def insert(self, index: int, item: Movie) -> None:
        """Insert item."""
        for i, filtered_item in enumerate(self._filtered()):
            if filtered_item == item:
                self.notify('insert', index=i, item=item)

    def pre_remove(self, index: int, item: Movie) -> None:
        """Pre remove."""
        for i, filtered_item in enumerate(self._filtered()):
            if filtered_item == item:
                # Track that the object *was* in the data source
                self._removals[item] = i

    def remove(self, index: int, item: Movie) -> None:  # noqa: F811
        """Remove item."""
        try:
            index = self._removals.pop(item)
            self.notify('remove', index=index, item=item)
        except KeyError:
            # object wasn't previously in the data source
            pass

    def clear(self: Self) -> None:  # noqa: F811
        """Clear source."""
        self.notify('clear')


class TableSourceWidgets:
    """Table source widgets."""

    def __init__(self) -> None:
        """Construct the widgets."""
        super().__init__()
        self.label_title = toga.Label('Ready.')

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

        # fmt: off
        # Buttons
        btn_style = Pack(flex=1)
        self.btn_insert = toga.Button('Insert Row', on_press=self.insert_handler, style=btn_style)  # noqa: E501
        self.btn_delete = toga.Button('Delete Row', on_press=self.delete_handler, style=btn_style)  # noqa: E501
        self.btn_clear = toga.Button('Clear Table', on_press=self.clear_handler, style=btn_style)  # noqa: E501
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        # fmt: on

    #####################################################################
    # Table callback functions
    def on_select_handler(self, widget: toga.Widget) -> None:
        """Handle on select."""
        row = widget.selection
        self.label_title.text = (
            f'You selected row: {row.title}'
            if row is not None
            else 'No row selected'
        )

    #####################################################################
    # Button callback functions
    def insert_handler(self, _: toga.Widget) -> None:
        """Insert the item."""
        self.table1.data.add(choice(bee_movies))

    def delete_handler(self, _: toga.Widget) -> None:
        """Delete the item."""
        if self.table1.selection:
            self.table1.data.remove(self.table1.selection)
        elif len(self.table1.data) > 0:
            self.table1.data.remove(self.table1.data[0])
        else:
            print('INFO: Table is empty!')

    def clear_handler(self, _: toga.Widget) -> None:
        """Clear the source."""
        self.table1.data.clear()


class TableSourceLayout(TableSourceWidgets, toga.Box):
    """Table source layout."""

    def __init__(self) -> None:
        """Construct the layout."""
        super().__init__()
        self.style.direction = COLUMN

        box_table = toga.Box(style=Pack(flex=1))
        box_btn = toga.Box(style=Pack(flex=1))

        # DOM
        self.add(
            self.label_title,
            box_table,
            box_btn,
            self.btn_goto_back,
        )
        box_table.add(
            self.table1,
            self.table2,
        )
        box_btn.add(
            self.btn_insert,
            self.btn_delete,
            self.btn_clear,
        )
