import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.executor import execute_script

def test_execute_script_custom_price():
    script = "price = get_price('BTC/USDT'); signal = 'buy' if price > 10 else 'sell'"
    result = execute_script(script, price_func=lambda s: 20)
    assert result == 'buy'
