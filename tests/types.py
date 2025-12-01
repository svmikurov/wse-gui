"""Defines type vars."""

from typing import TypedDict


class IdNameT(TypedDict):
    """Dict representation of choice with its 'name' and 'ID'."""

    id: int
    name: str


class CodeNameT(TypedDict):
    """Dict representation of choice with machine and human values."""

    code: str
    name: str


# Word study Presentation types
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PresentationOptionsT(TypedDict):
    """Fields type for Word study options."""

    categories: list[IdNameT]
    marks: list[IdNameT]
    sources: list[IdNameT]
    periods: list[IdNameT]
    translation_orders: list[CodeNameT]


class SelectedParametersT(TypedDict):
    """Fields type for Word study selected parameters."""

    category: IdNameT | None
    mark: IdNameT | None
    word_source: IdNameT | None
    translation_order: CodeNameT | None
    start_period: IdNameT | None
    end_period: IdNameT | None


class PresentationSettingsT(TypedDict):
    """Fields type for Word study presentation settings."""

    word_count: int | None
    question_timeout: int | None
    answer_timeout: int | None


class InitialParametersT(
    SelectedParametersT,
    PresentationSettingsT,
):
    """Fields type for Word study initial parameters."""


class WordPresentationParamsT(
    PresentationOptionsT,
    SelectedParametersT,
    PresentationSettingsT,
):
    """Fields type for Word study parameters."""
