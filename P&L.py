from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
user_portfolio = []  # Our empty master storage for user trades

class TradePosition(BaseModel):
    ticker: str
    shares: int
    buy_price: float

@app.post("/positions")
def add_position(position: TradePosition):
    user_portfolio.append(position)
    
    return {"status": "success", "message": "Position logged successfully!"}

@app.get("/portfolio")
def get_portfolio():
    latest_market_prices = {"AAPL": 225.00, "MSFT": 415.00}
    total_portfolio_pl = 0.0  # Accumulator bucket for overall profit
    
    for position in user_portfolio:
        clean_ticker = position.ticker.upper()
        
        # Grab the current market price safely
        current_price = latest_market_prices.get(clean_ticker, position.buy_price)
        
        # ───► YOUR CHALLENGE: Write the formula to calculate this position's P&L
        # Formula: (current_price - position.buy_price) * position.shares
        position_pl = (current_price - position.buy_price) * position.shares
        
        # Add this position's profit to our master accumulator bucket total
        total_portfolio_pl = total_portfolio_pl + position_pl
        
    return {"status": "success", "total_unrealized_pl": total_portfolio_pl}

