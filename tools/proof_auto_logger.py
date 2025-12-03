from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import json
import time


def log_proof(event: Dict[str, Any]) -> Path:
    Path("proof").mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%dT%H%M%S")
    path = Path("proof") / f"slim_proof_{ts}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(event, f, ensure_ascii=False, indent=2)
    print(f"🧾 proof written → {path}")
    return path
