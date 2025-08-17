# FinSight\data_processing\stock_fetcher.py
import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load API key from root .env automatically
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
API_KEY = os.getenv("ALPHA_VANTAGE_KEY")

def fetch_stock_data(symbol="AAPL"):
    """
    AUTOMATED STOCK DATA FETCHER
    Fetches 5 years of daily data with one function call
    """
    # Build API URL (auto-formatting)
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}&datatype=csv"
    
    # Magic one-line download and cache
    df = pd.read_csv(url)
    
    # Auto-save to CSV (creates file if doesn't exist)
    df.to_csv(f"data_processing/{symbol}_data.csv", index=False)
    print(f"✅ Success! {symbol} data saved!")
    return df

# Test run with Apple stock (will work immediately)
if __name__ == "__main__":
    fetch_stock_data()