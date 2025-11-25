# Credit Card Bonuses API Tool

This is a FastAPI application that serves credit card bonus offers from the GitHub dataset. 
It supports multiple query filters (bank, category, min_bonus, max_bonus, and card name).

## Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn credit_card_tool:app --host 0.0.0.0 --port 8000
```

## Example Queries

All cards: `http://localhost:8000/cards`

Filter by bank: `http://localhost:8000/cards?bank=Chase`

Filter by min bonus: `http://localhost:8000/cards?min_bonus=500`

Multiple filters: `http://localhost:8000/cards?bank=Chase&min_bonus=500&category=Travel`
