"""Foreign discipline API Request payload types."""

from dataclasses import dataclass, field
from decimal import Decimal


# TODO: Move for shared
@dataclass
class IdName:
    """Represents a basic identifiable entity with ID and name."""

    id: int
    name: str


# TODO: Move to data
@dataclass
class ParamsChoices:
    """Word study Presentation params choices.

    Included in Word study Presentation params Response data.
    """

    categories: list[IdName] = field(default_factory=list)
    marks: list[IdName] = field(default_factory=list)


# TODO: Move to data
@dataclass
class InitialParams:
    """Initial Word study Presentation params.

    Included in Word study Presentation params
    Request to update and Response to get data.
    """

    category: IdName | None = None
    mark: IdName | None = None
    word_source: IdName | None = None
    order: IdName | None = None
    start_period: IdName | None = None
    end_period: IdName | None = None


# TODO: Move to data
@dataclass
class Settings:
    """Word study Presentation params DTO."""

    word_count: Decimal | int | None = None
    question_timeout: Decimal | float | None = None
    answer_timeout: Decimal | float | None = None


# TODO: Move to data
@dataclass
class PresentationParamsDTO(
    InitialParams,
    ParamsChoices,
    Settings,
):
    """Presentation params with choices DTO."""
