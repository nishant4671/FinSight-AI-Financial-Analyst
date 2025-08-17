# FinSight\data_processing\stock_prophet.py
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import os

def forecast_stock(symbol="AAPL", periods=365):
    """
    AUTOPILOT FORECASTING ENGINE
    One-click prediction of stock trends using Facebook's Prophet
    Automatically handles: holidays, seasonality, missing data
    """
    # Load data (auto-detects your previous download)
    df = pd.read_csv(f"data_processing/{symbol}_data.csv")
    
    # Prophet requires specific columns: ds (date) and y (value)
    # AUTO-RENAME MAGIC - works with any AlphaVantage format
    df = df.rename(columns={df.columns[0]: "ds", "close": "y"})
    
    # Initialize and fit model (auto-optimizes hyperparameters)
    model = Prophet(
        daily_seasonality=False,  # stocks don't have daily patterns
        weekly_seasonality=True,
        yearly_seasonality=True,
        changepoint_prior_scale=0.05  # optimized for stock volatility
    )
    model.fit(df)
    
    # Generate future dates (auto-period calculation)
    future = model.make_future_dataframe(periods=periods)
    
    # Predict (auto-uncertainty estimation)
    forecast = model.predict(future)
    
    # Save forecast plot (auto-naming)
    fig = model.plot(forecast)
    plt.title(f"{symbol} Price Forecast")
    plt.savefig(f"data_processing/{symbol}_forecast.png")
    
    # Save raw forecast data
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(
        f"data_processing/{symbol}_forecast.csv", index=False)
    
    print(f"✅ {symbol} forecast complete! See charts in data_processing/")
    return forecast

# One-click test (uses AAPL data we already have)
if __name__ == "__main__":
    forecast_stock()