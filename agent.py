"""Reproducible RSI and moving-average signal reviewer; never executes trades."""
from __future__ import annotations


def _rsi(prices: list[float], period: int = 14) -> float | None:
    if len(prices) <= period:
        return None
    changes = [b - a for a, b in zip(prices[-period - 1:-1], prices[-period:])]
    gain = sum(max(change, 0) for change in changes) / period
    loss = sum(max(-change, 0) for change in changes) / period
    if loss == 0:
        return 100.0
    return round(100 - 100 / (1 + gain / loss), 2)


def review_signal(prices: list[float], short_window: int = 5, long_window: int = 20) -> dict:
    values = [float(value) for value in prices]
    if len(values) < long_window:
        return {"signal": "insufficient-data", "required_points": long_window, "available_points": len(values), "human_review_required": True}
    short_ma = round(sum(values[-short_window:]) / short_window, 4)
    long_ma = round(sum(values[-long_window:]) / long_window, 4)
    rsi = _rsi(values)
    signal = "review-buy" if short_ma > long_ma and rsi is not None and rsi < 70 else "review-sell" if short_ma < long_ma and rsi is not None and rsi > 30 else "hold-review"
    return {"signal": signal, "evidence": {"last_price": values[-1], "short_ma": short_ma, "long_ma": long_ma, "rsi_14": rsi, "observations": len(values)}, "limitations": ["Historical indicators do not predict future returns.", "Costs, slippage, liquidity, news, and taxes are not modeled."], "trade_executed": False, "human_review_required": True}
