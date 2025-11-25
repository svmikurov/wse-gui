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
# -----------------------------


class ParamOptionsT(TypedDict):
    """Fields type for Word study Parameter options."""

    categories: list[IdNameT] | None
    marks: list[IdNameT] | None
    sources: list[IdNameT] | None
    periods: list[IdNameT]
    translation_orders: list[CodeNameT]


class InitialChoicesT(TypedDict):
    """Fields type for Word study Parameter initial choices."""

    category: IdNameT | None
    mark: IdNameT | None
    word_source: IdNameT | None
    translation_order: CodeNameT | None
    start_period: IdNameT | None
    end_period: IdNameT | None


class PresentationSettingsT(TypedDict):
    """Fields type for Word study parameter settings."""

    word_count: int | None
    question_timeout: float | None
    answer_timeout: float | None


class WordPresentationParamsT(
    ParamOptionsT,
    InitialChoicesT,
    PresentationSettingsT,
):
    """Fields type for Word study parameters."""
