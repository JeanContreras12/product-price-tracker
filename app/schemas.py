from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    url: str

class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True
