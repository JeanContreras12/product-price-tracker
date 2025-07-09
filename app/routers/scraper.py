from fastapi import APIRouter
from app.scraper import update_prices

router_scraper = APIRouter(prefix="/scraper", tags=["Scraper"])

@router_scraper.get("/")
def run_scraper():
    update_prices()
    return {"message": "Scraping completado"}
