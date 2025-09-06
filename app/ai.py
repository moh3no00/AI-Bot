"""ابزارهای تحلیل هوشمند بازار"""

from typing import Sequence


def _rsi(values: Sequence[float], period: int = 14) -> float:
    """محاسبه شاخص قدرت نسبی (RSI)"""
    if len(values) < period + 1:
        return 50.0
    gains = []
    losses = []
    for i in range(1, period + 1):
        diff = values[-i] - values[-i - 1]
        if diff >= 0:
            gains.append(diff)
        else:
            losses.append(abs(diff))
    avg_gain = sum(gains) / period if gains else 0.0
    avg_loss = sum(losses) / period if losses else 1.0
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def analyze_series(prices: Sequence[float]) -> dict:
    """تحلیل روند قیمت با رگرسیون خطی و شاخص RSI"""
    values = [float(p) for p in prices]
    n = len(values)
    if n == 0:
        return {"signal": "none", "slope": 0.0, "rsi": 50.0}

    # محاسبه شیب روند با رگرسیون خطی
    x_vals = list(range(n))
    mean_x = sum(x_vals) / n
    mean_y = sum(values) / n
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_vals, values))
    den = sum((x - mean_x) ** 2 for x in x_vals) or 1.0
    slope = num / den

    # محاسبه RSI
    rsi_value = _rsi(values)

    # تعیین سیگنال بر اساس شیب و RSI
    if slope > 0 and rsi_value < 70:
        signal = "buy"
    elif slope < 0 and rsi_value > 30:
        signal = "sell"
    else:
        signal = "hold"

    return {"signal": signal, "slope": slope, "rsi": rsi_value}
