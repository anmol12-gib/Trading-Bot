from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

class BinanceClient:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API keys not found")

        
        self.client = Client(api_key, api_secret, testnet=True)

    def create_order(self, **params):
        return self.client.futures_create_order(**params)
