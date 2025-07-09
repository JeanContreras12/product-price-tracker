import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from datetime import datetime
from app import models
from app.database import SessionLocal

def fetch_price_from_url(url: str) -> float | None:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Este selector cambiará según el sitio
        price_text = soup.select_one(".price").text.strip().replace("$", "").replace(".", "").replace(",", ".")
        return float(price_text)
    except Exception as e:
        print(f"Error al hacer scraping de {url}: {e}")
        return None

def update_prices():
    db: Session = SessionLocal()
    products = db.query(models.Product).all()

    for product in products:
        price = fetch_price_from_url(product.url)
        if price is not None:
            # Agregar a la tabla de historial
            history = models.PriceHistory(
                product_id=product.id,
                price=price,
                timestamp=datetime.utcnow()
            )
            db.add(history)

            # Actualizar precio actual
            product.price = price
            db.commit()
            db.refresh(product)
            print(f"Precio actualizado: {product.name} - ${price}")

    db.close()
