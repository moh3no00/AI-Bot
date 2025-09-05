import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.risk import RiskManager


def test_risk_manager():
    rm = RiskManager(stop_loss=90, take_profit=110)
    assert rm.check(100, 85) == "stop_loss"
    assert rm.check(100, 120) == "take_profit"
    assert rm.check(100, 100) == "hold"
