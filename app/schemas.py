from pydantic import BaseModel, field_validator, Field
class UserInput(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int = Field(gt=0)
    total_rooms: int = Field(gt=0)
    total_bedrooms: int = Field(gt=0)
    population: int = Field(gt=0)
    households: int = Field(gt=0)
    median_income: float = Field(gt=0)
    ocean_proximity: str

    @field_validator('ocean_proximity')
    @classmethod
    def validate_proximity(self, value):
        value = value.upper()
        valid_proximities = ("NEAR BAY", "<1H OCEAN", "INLAND", "NEAR OCEAN", "ISLAND")

        if value not in valid_proximities:
            raise ValueError("Invalid Ocean Proximity")
