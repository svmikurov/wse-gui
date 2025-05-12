"""Defines contextmanager."""

from contextlib import contextmanager
from typing import Iterator

from wse.features.shared.enums import FieldID
from wse.interface.iobserver import ISubject, ISubjectWithID


@contextmanager
def temporarily_disable_on_change_call(
    subject: ISubject | ISubjectWithID, field_id: FieldID
) -> Iterator[None]:
    """Temporarily disable subject's notifications for given field."""
    subject.notify('temporarily_disable', action='disable', field_id=field_id)
    try:
        yield
    finally:
        subject.notify(
            'temporarily_disable', action='enable', field_id=field_id
        )
