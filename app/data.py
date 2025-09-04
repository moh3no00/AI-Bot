import ccxt
import yfinance as yf
import pandas as pd
from typing import List


def get_crypto_tickers(limit: int = 50) -> pd.DataFrame:
    """دریافت لیست رمز ارزها از صرافی بایننس"""
    exchange = ccxt.binance()
    markets = exchange.load_markets()
    symbols = list(markets.keys())[:limit]
    tickers = exchange.fetch_tickers(symbols)
    records = []
    for sym, data in tickers.items():
        records.append({
            "symbol": sym,
            "price": data.get("last"),
            "change": data.get("percentage"),
        })
    return pd.DataFrame(records)


def get_commodity_prices() -> pd.DataFrame:
    """دریافت قیمت لحظه‌ای طلا، نقره و نفت از یاهو فایننس"""
    tickers = {
        "طلا": "GC=F",
        "نقره": "SI=F",
        "نفت": "CL=F",
    }
    rows = []
    for name, t in tickers.items():
        data = yf.Ticker(t).history(period="1d")
        price = data["Close"].iloc[-1]
        rows.append({"symbol": name, "price": price})
    return pd.DataFrame(rows)
