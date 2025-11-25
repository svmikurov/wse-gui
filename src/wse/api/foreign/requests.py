"""Foreign discipline API Request payload types."""

from dataclasses import dataclass, field


# TODO: Move for shared
@dataclass
class IdName:
    """Represents a basic identifiable entity with ID and name."""

    id: int
    name: str


@dataclass
class CodeName:
    """Represents a basic identifiable entity with code and name."""

    code: str
    name: str


@dataclass
class ParameterOptions:
    """Word study Presentation parameter options."""

    categories: list[IdName] = field(default_factory=list)
    marks: list[IdName] = field(default_factory=list)
    sources: list[IdName] = field(default_factory=list)
    periods: list[IdName] = field(default_factory=list)
    translation_orders: list[CodeName] = field(default_factory=list)


@dataclass
class SelectedParameters:
    """Selected Word study Presentation parameters."""

    category: IdName | None = None
    mark: IdName | None = None
    word_source: IdName | None = None
    translation_order: CodeName | None = None
    start_period: IdName | None = None
    end_period: IdName | None = None


@dataclass
class SettingParameters:
    """Word study Presentation parameter settings."""

    word_count: int | None = None
    question_timeout: int | None = None
    answer_timeout: int | None = None


@dataclass
class InitialParametersDTO(
    SelectedParameters,
    SettingParameters,
):
    """Word study Presentation initial parameters DTO."""


@dataclass
class PresentationParamsDTO(
    SelectedParameters,
    ParameterOptions,
    SettingParameters,
):
    """Presentation params with choices DTO."""
