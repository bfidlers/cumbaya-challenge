from pydantic import BaseModel, Field


class TripRequest(BaseModel):
    city: str
    country_code: str = Field(min_length=2, max_length=2)
    adults: int = Field(gt=0)
    children_ages: list[int] = []