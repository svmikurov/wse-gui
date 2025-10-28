"""Data Transfer Object (DTO) types for Foreign Discipline module."""

# TODO: Remove?

from typing import NamedTuple


class IdNameDTO(NamedTuple):
    """DTO representation of entity only with its 'name' and 'ID'."""

    id: int
    name: str


class SelectionsWordParamsDTO(NamedTuple):
    """Selections of Word study params DTO."""

    categories: list[IdNameDTO]
    labels: list[IdNameDTO]


class CaseWordParamsDTO(NamedTuple):
    """Case of Word study params DTO."""

    category: IdNameDTO
    name: IdNameDTO
