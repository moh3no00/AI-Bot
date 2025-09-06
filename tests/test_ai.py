import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.ai import analyze_series


def test_analyze_series_buy():
    prices = [1, 2, 3, 4, 5]
    result = analyze_series(prices)
    assert result["signal"] == "buy"


def test_analyze_series_rsi_range():
    prices = list(range(1, 30))
    result = analyze_series(prices)
    assert 0 <= result["rsi"] <= 100
    assert isinstance(result["slope"], float)
