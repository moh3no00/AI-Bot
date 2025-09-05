import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.executor import execute_script
from app.risk import RiskManager


def test_execute_script_custom_price():
    script = "price = get_price('BTC/USDT'); signal = 'buy' if price > 10 else 'sell'"
    result = execute_script(script, price_func=lambda s: 20)
    assert result == 'buy'


def test_execute_script_with_risk():
    script = "status = risk.check(100, 80); signal = 'exit' if status != 'hold' else 'hold'"
    rm = RiskManager(90, 110)
    result = execute_script(script, price_func=lambda s: 20, risk=rm)
    assert result == 'exit'
