"""Model data validation."""

from decimal import Decimal

from pydantic import BaseModel

class IndexData(BaseModel):
    """Math index data app response model."""

    balance: Decimal | None
    exercises: list[str]
