# FinSight/data_processing/full_analysis.py
import sys
import os

# Print debugging information
print("Current directory:", os.getcwd())
print("Python path:", sys.path)
print("Files in directory:", os.listdir())


import sys
import json
import os
from dotenv import load_dotenv

# Load environment variables from root .env
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Import analysis modules
try:
    from stock_fetcher import fetch_stock_data
    from stock_prophet import forecast_stock
    from sentiment_analyzer import run_sentiment_analysis
    from report_generator import generate_financial_report
except ImportError as e:
    print(f"❌ Import error: {str(e)}")
    sys.exit(1)

def main(symbol):
    """Orchestrates the full analysis pipeline"""
    try:
        # Step 1: Fetch data
        print(f"📥 Fetching data for {symbol}...")
        fetch_stock_data(symbol)
        
        # Step 2: Generate forecast
        print("🔮 Generating forecast...")
        forecast_df = forecast_stock(symbol)
        
        # Step 3: Analyze sentiment
        print("📰 Analyzing market sentiment...")
        sentiment_score, sentiment_label = run_sentiment_analysis(symbol)
        
        # Step 4: Generate report
        print("📊 Creating financial report...")
        report = generate_financial_report(
            ticker=symbol,
            forecast_csv_path=f"data_processing/{symbol}_forecast.csv",
            sentiment_score=sentiment_score,
            sentiment_label=sentiment_label
        )
        
        # Prepare output for Node.js
        return {
            "symbol": symbol,
            "forecast_chart": f"{symbol}_forecast.png",
            "sentiment": sentiment_label,
            "sentiment_score": sentiment_score,
            "report": report
        }
        
    except Exception as e:
        print(f"❌ Analysis pipeline failed: {str(e)}")
        return {"error": str(e)}

if __name__ == "__main__":
    # Get symbol from command line argument
    symbol = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    
    try:
        result = main(symbol)
        # Output as JSON string for Node.js
        print(json.dumps(result))
    except Exception as e:
        error_result = {"error": f"Critical failure: {str(e)}"}
        print(json.dumps(error_result))
        sys.exit(1)