"""Defines data model fo Calculation page."""

import uuid

from pydantic import BaseModel
from wse_exercises.base.mixins import ConvertMixin

# TODO: Fix combined `ConvertMixin` and `BaseModel` to `BaseSchema'


class CalcConfDTO(ConvertMixin, BaseModel):
    """Calculation task config DTO."""

    min_value: str
    max_value: str


class CalcDataDTO(ConvertMixin, BaseModel):
    """Calculation exercise data model."""

    exercise_name: str


class CalcTaskDTO(ConvertMixin, BaseModel):
    """Calculation task DTO."""

    uid: uuid.UUID
    question: str


class CalcAnswerDTO(ConvertMixin, BaseModel):
    """Calculation task user answer DTO."""

    uid: uuid.UUID
    answer: str


class CalcResultDTO(ConvertMixin, BaseModel):
    """Calculation task user answer checking result DTO."""

    is_correct: bool
    correct_answer: str
