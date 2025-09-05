import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.ai import analyze_series, generate_strategy
from app.executor import execute_script

def test_analyze_series_buy():
    prices = [1, 2, 3, 4, 5]
    result = analyze_series(prices)
    assert result["signal"] == "buy"


def test_generate_strategy_buy_command():
    cmd = "اگر قیمت BTC/USDT بیشتر از 20000 شد بخر"
    script = generate_strategy(cmd)
    signal = execute_script(script, price_func=lambda s: 21000)
    assert signal == "buy"
