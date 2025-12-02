"""Foreign discipline API Request payload types."""

from dataclasses import dataclass, field, fields
from typing import Self, TypeAlias, Union

Options: TypeAlias = list['IdName'] | list['CodeName']
Selected: TypeAlias = Union['IdName', 'CodeName']
WordOptions: TypeAlias = Options | Selected

# Nested
# ------


@dataclass(frozen=True)
class IdName:
    """Represents a basic identifiable entity with ID and name."""

    id: str
    name: str


@dataclass(frozen=True)
class CodeName:
    """Represents a basic identifiable entity with code and name."""

    code: str
    name: str


# Base
# ----


@dataclass(frozen=True)
class ParameterOptions:
    """Word study Presentation parameter options."""

    categories: list[IdName] = field(default_factory=list)
    marks: list[IdName] = field(default_factory=list)
    sources: list[IdName] = field(default_factory=list)
    periods: list[IdName] = field(default_factory=list)
    translation_orders: list[CodeName] = field(default_factory=list)


@dataclass(frozen=True)
class SelectedParameters:
    """Selected Word study Presentation parameters."""

    category: IdName | None = None
    mark: IdName | None = None
    word_source: IdName | None = None
    translation_order: CodeName | None = None
    start_period: IdName | None = None
    end_period: IdName | None = None


@dataclass(frozen=True)
class SetParameters:
    """Word study set parameters."""

    word_count: int | None = None


@dataclass(frozen=True)
class PresentationSettings:
    """Word study Presentation settings."""

    question_timeout: int | None = None
    answer_timeout: int | None = None


# DTO
# ---


@dataclass(frozen=True)
class InitialParameters(
    SelectedParameters,
    SetParameters,
    PresentationSettings,
):
    """Word study Presentation initial parameters DTO."""

    @classmethod
    def from_dto(
        cls,
        dto: SelectedParameters | SetParameters | PresentationSettings,
    ) -> Self:
        """Create initial parameters DTO."""
        return cls(
            **{
                field.name: getattr(dto, field.name, None)
                for field in fields(cls)
            }
        )


@dataclass(frozen=True)
class PresentationParameters(
    ParameterOptions,
    SelectedParameters,
    SetParameters,
    PresentationSettings,
):
    """Presentation params with choices DTO."""
