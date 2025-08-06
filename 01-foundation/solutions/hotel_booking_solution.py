from pydantic import BaseModel,fields, model_validator, computed_field

class HotelBooking(BaseModel):
    user_id: int
    room_id: int
    nights: int = fields(..., ge=1)
    rate_per_nights: int

    @model_validator(mode='after')
    def validate_nights(cls, values):
        if values.nights < 1:
            raise ValueError("Nights must be at least 1")
        return values

    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights * self.rate_per_nights