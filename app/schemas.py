from pydantic import BaseModel, field_validator

class UserInput(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: float
    median_house_value: int
    ocean_proximity: str

    @field_validator('ocean_proximity')
    @classmethod
    def validate_proximity(self, value):
        value = value.upper()
        valid_proximities = ["NEAR BAY", "<1H OCEAN", "INLAND", "NEAR OCEAN", "ISLAND"]

        if value not in valid_proximities:
            raise ValueError("Invalid Ocean Proximity")
