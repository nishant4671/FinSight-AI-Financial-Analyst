# FinSight\genai_core\report_generator.py
import os
from openai import OpenAI  # NEW IMPORT STYLE
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

def generate_financial_report(ticker="AAPL", sentiment="Bullish"):
    """
    UPDATED REPORT GENERATOR FOR OPENAI v1.x+
    Uses the new client-based API structure
    """
    try:
        # Initialize client with API key
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Create prompt
        prompt = f"""Create a professional investment report for {ticker} stock. 
        Context: Market sentiment is {sentiment}. 
        Structure:
        1. EXECUTIVE SUMMARY
        2. TECHNICAL ANALYSIS 
        3. RISK ASSESSMENT
        4. RECOMMENDATION
        Use professional financial language."""
        
        # Call OpenAI API - NEW SYNTAX
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=300
        )
        
        # Extract content - NEW ACCESS METHOD
        report = response.choices[0].message.content.strip()
        
        # Save report
        today = datetime.now().strftime("%Y%m%d")
        with open(f"../data_processing/{ticker}_report_{today}.txt", 'w') as f:
            f.write(report)
            
        print(f"✅ Report generated successfully using OpenAI v1.x API!")
        return report
        
    except Exception as e:
        print(f"❌ API Error: {str(e)}")
        return "Report generation failed."

# Test run
if __name__ == "__main__":
    generate_financial_report()