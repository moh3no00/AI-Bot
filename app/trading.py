import ccxt
from typing import Dict


class ExchangeManager:
    def __init__(self):
        self.connections: Dict[str, ccxt.Exchange] = {}

    def connect(self, name: str, api_key: str, secret: str):
        exchange_class = getattr(ccxt, name)
        exchange = exchange_class({
            "apiKey": api_key,
            "secret": secret,
        })
        exchange.load_markets()
        self.connections[name] = exchange
        return exchange

    def get(self, name: str) -> ccxt.Exchange:
        return self.connections[name]
