# FinSight\genai_core\report_generator.py
import os
import openai
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_financial_report(ticker="AAPL", sentiment="Bullish"):
    """
    LIGHTWEIGHT REPORT GENERATOR
    Uses only OpenAI API - no external dependencies
    """
    try:
        # Create prompt with mock data
        prompt = f"""Create a professional investment report for {ticker} stock. 
        Context: Market sentiment is {sentiment}. 
        Structure:
        1. EXECUTIVE SUMMARY
        2. TECHNICAL ANALYSIS 
        3. RISK ASSESSMENT
        4. RECOMMENDATION
        Use professional financial language."""
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=300
        )
        
        # Save report
        report = response.choices[0].message['content'].strip()
        today = datetime.now().strftime("%Y%m%d")
        with open(f"../data_processing/{ticker}_report_{today}.txt", 'w') as f:
            f.write(report)
            
        print(f"✅ Report generated successfully!")
        return report
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return "Report generation failed."

# Test run
if __name__ == "__main__":
    generate_financial_report()