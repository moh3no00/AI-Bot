import json
from pathlib import Path
from typing import Dict

SETTINGS_FILE = Path(__file__).parent / "settings.json"


def load_settings() -> Dict:
    if SETTINGS_FILE.exists():
        return json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    return {"exchanges": {}, "brokers": {}}


def save_settings(data: Dict):
    SETTINGS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
