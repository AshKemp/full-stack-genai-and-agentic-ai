from pydantic import BaseModel, field_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name','last_name')
    def names_must_be_capitalized(cls,val):
        if not val.isTitle():
            raise ValueError('Names must be capitalized')
        return val

class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls,val):
        return val.lower().strip()
    

class Product(BaseModel):
    price: str # $4.44 

    @field_validator('price',mode="before")
    def parse_price(cls,val):
        if isinstance(val,str):
            return float(val.replace('$',''))
        return val

                     
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError('end_date must be after start_date')
        return values                     