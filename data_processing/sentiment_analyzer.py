# FinSight\data_processing\sentiment_analyzer.py
import os
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from transformers import pipeline
from dotenv import load_dotenv
import torch  # Required for FinBERT

# Load environment variables from root .env
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

def fetch_financial_news(ticker="AAPL", num_articles=5):
    """
    AUTOMATED NEWS SCRAPER
    Fetches recent financial news headlines for a stock
    Uses Google News RSS feed for reliability
    """
    try:
        # Build Google News URL
        url = f"https://news.google.com/rss/search?q={ticker}+stock&hl=en-US&gl=US&ceid=US:en"
        
        # Fetch RSS feed
        response = requests.get(url)
        response.raise_for_status()  # Throw error for bad status
        
        # Parse XML
        soup = BeautifulSoup(response.text, 'xml')
        items = soup.find_all('item')[:num_articles]
        
        # Extract headlines
        headlines = []
        for item in items:
            title = item.title.text
            # Clean headline (remove source tags)
            clean_title = re.sub(r' - [^-]+$', '', title)
            headlines.append(clean_title)
        
        return headlines
    
    except Exception as e:
        print(f"❌ News fetch error: {e}")
        return ["Market shows mixed signals"]  # Fallback headline

def analyze_sentiment(headlines):
    """
    FINBERT SENTIMENT ANALYSIS
    Uses specialized financial NLP model
    Returns sentiment score (-1 to 1) and label
    """
    try:
        # Initialize FinBERT - automatically downloads model first time
        # 'finbert' is pre-trained on financial documents
        classifier = pipeline(
            "text-classification", 
            model="ProsusAI/finbert", 
            tokenizer="ProsusAI/finbert"
        )
        
        # Analyze all headlines
        results = classifier(headlines)
        
        # Calculate average sentiment
        sentiment_sum = 0
        for result in results:
            # Convert LABEL to score: positive=1, negative=-1, neutral=0
            if result['label'] == 'positive':
                sentiment_sum += 1
            elif result['label'] == 'negative':
                sentiment_sum -= 1
        
        avg_sentiment = sentiment_sum / len(headlines)
        
        # Determine overall sentiment
        if avg_sentiment > 0.2:
            return avg_sentiment, "Bullish 🚀"
        elif avg_sentiment < -0.2:
            return avg_sentiment, "Bearish 🐻"
        else:
            return avg_sentiment, "Neutral 😐"
            
    except Exception as e:
        print(f"❌ Sentiment analysis error: {e}")
        return 0.0, "Neutral 😐"  # Fallback value

def run_sentiment_analysis(ticker="AAPL"):
    """
    END-TO-END SENTIMENT PIPELINE
    Combines news scraping and sentiment analysis
    """
    print(f"⏳ Fetching news for {ticker}...")
    headlines = fetch_financial_news(ticker)
    
    if not headlines:
        print("⚠️ Using fallback headlines")
        headlines = ["Market analysis unavailable"]
    
    print(f"🔍 Analyzing sentiment across {len(headlines)} headlines...")
    score, label = analyze_sentiment(headlines)
    
    # Print results table
    print("\n📰 Latest Headlines:")
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")
    
    print(f"\n✅ Final Sentiment: {label} ({score:.2f})")
    return score, label

# Test run
if __name__ == "__main__":
    run_sentiment_analysis()