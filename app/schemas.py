from datetime import datetime
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    url: str

class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True
class PriceHistory(BaseModel):
    id: int
    product_id: int
    price: float
    timestamp: datetime

    class Config:
        orm_mode = True