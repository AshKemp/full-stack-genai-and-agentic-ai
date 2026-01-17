from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []
    
    model_config = ConfigDict(
        json_encoders = {
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )

user = User(
    id=1,
    name="Ashwin",
    email="kmuraliashwin@gmail.com",
    createdAt=datetime(2026,1,17,12,30),
    address=Address(
        street="123 Main St",
        city="Springfield",
        zip_code="12345"
    ),
    is_active=False,
    tags=["admin", "user"]
)

python_dict = user.model_dump()
print(python_dict)

json_str = user.model_dump_json()
print("="*30)
print(json_str)
