import os
import sys

def main():
    print("=" * 50)
    print("ENVIRONMENT VARIABLES TEST")
    print("=" * 50)
    
    # Try to load .env file manually
    try:
        with open('.env', 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value
                    print(f"Loaded from .env: {key}={value[:4]}...")
    except FileNotFoundError:
        print(".env file not found")
    
    # Check variables
    print(f"\nPORT: {os.getenv('PORT', 'Not found')}")
    print(f"NODE_ENV: {os.getenv('NODE_ENV', 'Not found')}")
    print(f"ALPHA_VANTAGE_KEY: {os.getenv('ALPHA_VANTAGE_KEY', 'Not found')}")
    print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY', 'Not found')}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()