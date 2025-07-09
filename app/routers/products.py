from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from typing import List
from app.scraper import update_prices

router_products = APIRouter(prefix="/products", tags=["Products"])

# Crear producto
@router_products.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    # Guardar el precio histórico inicial
    price_entry = models.PriceHistory(
        product_id=db_product.id,
        price=db_product.price
    )
    db.add(price_entry)
    db.commit()
    return db_product

# Obtener todos los productos
@router_products.get("/", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

# Obtener un producto por ID
@router_products.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

# Actualizar un producto
@router_products.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, updated: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    for key, value in updated.dict().items():
        setattr(product, key, value)
    
    db.commit()
    db.refresh(product)
    return product

# Eliminar un producto
@router_products.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(product)
    db.commit()
@router_products.get("/{product_id}/history", response_model=List[schemas.PriceHistory])
def get_price_history(product_id: int, db: Session = Depends(get_db)):
    history = db.query(models.PriceHistory).filter(models.PriceHistory.product_id == product_id).all()
    if not history:
        raise HTTPException(status_code=404, detail="No hay historial para este producto")
    return history
