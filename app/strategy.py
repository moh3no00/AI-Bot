import json
from pathlib import Path
from typing import Dict, List

STRATEGY_FILE = Path(__file__).parent / "strategies.json"


def load_strategies() -> List[Dict]:
    if STRATEGY_FILE.exists():
        return json.loads(STRATEGY_FILE.read_text(encoding="utf-8"))
    return []


def save_strategies(strategies: List[Dict]):
    STRATEGY_FILE.write_text(json.dumps(strategies, ensure_ascii=False, indent=2), encoding="utf-8")


def add_strategy(
    name: str,
    script: str,
    market: str,
    asset: str,
    enabled: bool = True,
    stop_loss: float | None = None,
    take_profit: float | None = None,
    volume: float = 1.0,
):
    strategies = load_strategies()
    strategies.append(
        {
            "name": name,
            "script": script,
            "market": market,
            "asset": asset,
            "enabled": enabled,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "volume": volume,
        }
    )
    save_strategies(strategies)
