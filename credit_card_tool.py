from fastapi import FastAPI, Query
import requests

app = FastAPI(title="Credit Card Bonuses API Tool")

DATA_URL = "https://raw.githubusercontent.com/andenacitelli/credit-card-bonuses-api/main/exports/data.json"
cards = requests.get(DATA_URL).json()

@app.get("/cards")
def get_cards(
    bank: str = Query(None, description="Filter by bank name (partial match)"),
    category: str = Query(None, description="Filter by category (partial match)"),
    min_bonus: int = Query(None, description="Minimum bonus amount"),
    max_bonus: int = Query(None, description="Maximum bonus amount"),
    name: str = Query(None, description="Filter by card name (partial match)")
):
    """
    Return credit card offers with multiple optional filters
    """
    results = cards
    
    if bank:
        results = [c for c in results if bank.lower() in c.get("issuer", "").lower()]
    if category:
        results = [c for c in results if category.lower() in c.get("category", "").lower()]
    if min_bonus:
        results = [c for c in results if c.get("bonus_amount", 0) >= min_bonus]
    if max_bonus:
        results = [c for c in results if c.get("bonus_amount", 0) <= max_bonus]
    if name:
        results = [c for c in results if name.lower() in c.get("name", "").lower()]
    
    return results
