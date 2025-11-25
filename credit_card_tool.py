from fastapi import FastAPI, Query
import requests
from typing import List, Dict

app = FastAPI(title="Credit Card Bonuses API Tool")

DATA_URL = "https://raw.githubusercontent.com/andenacitelli/credit-card-bonuses-api/main/exports/data.json"
cards = requests.get(DATA_URL).json()

@app.get("/cards")
def get_cards(
    bank: str = Query(default="", description="Bank or issuer name. Partial matches allowed."),
    category: str = Query(default="", description="Category of the credit card offer. Partial matches allowed."),
    min_bonus: int = Query(default=0, description="Minimum bonus amount in dollars."),
    max_bonus: int = Query(default=10000, description="Maximum bonus amount in dollars."),
    name: str = Query(default="", description="Name of the credit card. Partial matches allowed."),
) -> List[Dict]:
    """
    Return credit card offers with multiple optional filters
    """
    results = cards
    
    if bank:
        results = [c for c in results if bank.lower() in c["issuer"].lower()]
    if category:
        results = [c for c in results if category.lower() in c["category"].lower()]
    if min_bonus > 0:
        results = [c for c in results if c["bonus_amount"] >= min_bonus]
    if max_bonus < 10000:
        results = [c for c in results if c["bonus_amount"] <= max_bonus]
    if name:
        results = [c for c in results if name.lower() in c["name"].lower()]

    return results
