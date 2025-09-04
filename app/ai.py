from typing import Sequence


def analyze_series(prices: Sequence[float]) -> dict:
    """تحلیل ساده روند قیمت با استفاده از رگرسیون خطی"""
    values = [float(p) for p in prices]
    n = len(values)
    if n == 0:
        return {"signal": "none", "slope": 0.0}
    x_vals = list(range(n))
    mean_x = sum(x_vals) / n
    mean_y = sum(values) / n
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_vals, values))
    den = sum((x - mean_x) ** 2 for x in x_vals) or 1.0
    slope = num / den
    signal = "buy" if slope > 0 else "sell"
    return {"signal": signal, "slope": slope}
