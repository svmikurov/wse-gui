"""Foreign discipline API Request payload types."""

from dataclasses import dataclass, field, fields
from typing import Generator, Literal, Self, TypeAlias, Union

Options: TypeAlias = list['IdName'] | list['CodeName']
Selected: TypeAlias = Union['IdName', 'CodeName']
WordOptions: TypeAlias = Options | Selected

OptionAccessor: TypeAlias = Literal[
    'category',
    'mark',
    'word_source',
    'start_period',
    'end_period',
    'translation_order',
]
InputAccessor: TypeAlias = Literal[
    'word_count',
    'question_timeout',
    'answer_timeout',
]
SwitchAccessor: TypeAlias = Literal[
    'is_study',
    'is_repeat',
    'is_examine',
    'is_know',
]
ParameterAccessors: TypeAlias = OptionAccessor | InputAccessor | SwitchAccessor

# Nested
# ------


@dataclass(frozen=True)
class IdName:
    """Represents a basic identifiable entity with ID and name."""

    id: str
    name: str


NOT_SELECTED = IdName(id='', name='-----')
"""Placeholder for selection with not selected options value.
"""


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

    is_study: bool | None = True
    is_repeat: bool | None = False
    is_examine: bool | None = False
    is_know: bool | None = False


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
    def extract_from(
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
    InitialParameters,
):
    """Presentation params with choices DTO."""

    @property
    def accessor_options(self) -> tuple[tuple[OptionAccessor, Options], ...]:
        """Get accessor options."""
        return (
            ('category', self.categories),
            ('mark', self.marks),
            ('word_source', self.sources),
            ('start_period', self.periods),
            ('end_period', self.periods),
            ('translation_order', self.translation_orders),
        )

    def iterate_initial(
        self,
    ) -> Generator[tuple[ParameterAccessors, Selected | int], None, None]:
        """Iterate by initial parameters."""
        for field_ in fields(InitialParameters):
            value = getattr(self, field_.name)
            if value is not None:
                yield field_.name, value  # type: ignore[misc]

    def iterate_options(
        self,
    ) -> Generator[tuple[OptionAccessor, Options], None, None]:
        """Iterate by accessor with options."""
        for accessor, options in self.accessor_options:
            match options:
                case [IdName(_, _), *_]:
                    values = [NOT_SELECTED, *options]

                case _:
                    values = options

            yield accessor, values

    @property
    def initial(self) -> InitialParameters:
        """Get initial parameters."""
        return InitialParameters.extract_from(self)
