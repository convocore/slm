# slm/utils/tracer.py
from __future__ import annotations
import json, time
from pathlib import Path
from typing import Any, Dict

class StudentTracer:
    def __init__(self, trace_dir: str, session_id: str):
        self.path = Path(trace_dir) / f"{session_id}.jsonl"

    def log(self, event: str, payload: Dict[str, Any]) -> None:
        rec = {
            "ts": time.time(),
            "event": event,
            "data": payload,
        }
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
