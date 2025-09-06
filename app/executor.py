import threading
from typing import Dict, Callable
from .strategy import load_strategies
from .risk import RiskManager


def default_price(symbol: str) -> float:
    from .data import get_crypto_tickers, get_commodity_prices

    df = get_crypto_tickers(500)
    row = df[df['symbol'] == symbol]
    if not row.empty:
        return float(row['price'])
    df = get_commodity_prices()
    row = df[df['symbol'] == symbol]
    if not row.empty:
        return float(row['price'])
    raise ValueError('symbol not found')


def execute_script(script: str, price_func: Callable[[str], float] = default_price, **context) -> str:
    """اجرای اسکریپت استراتژی با دسترسی به تابع قیمت"""
    local_vars = {"get_price": price_func, "signal": None}
    local_vars.update(context)
    exec(script, {}, local_vars)
    return local_vars.get("signal")


class StrategyExecutor:
    """اجرای همزمان استراتژی‌های فعال"""

    def __init__(self):
        self.results: Dict[str, str] = {}

    def _run(self, strategy: Dict):
        risk = RiskManager(strategy.get("stop_loss"), strategy.get("take_profit"))
        signal = execute_script(
            strategy["script"],
            asset=strategy.get("asset"),
            risk=risk,
            volume=strategy.get("volume", 1.0),
        )
        self.results[strategy["name"]] = signal

    def run_all(self) -> Dict[str, str]:
        strategies = [s for s in load_strategies() if s.get("enabled")]
        threads = []
        for s in strategies:
            t = threading.Thread(target=self._run, args=(s,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        return self.results
