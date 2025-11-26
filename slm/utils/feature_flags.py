# slm/utils/feature_flags.py
import os
from pathlib import Path
from typing import TypedDict

class StudentModeConfig(TypedDict, total=False):
    enabled: bool
    trace_dir: str
    note: str

def get_student_mode(cfg: dict | None) -> StudentModeConfig:
    # precedence: env > yaml > default
    env_on = os.getenv("SLM_STUDENT_MODE", "").strip() in {"1", "true", "on", "yes"}
    yml = (cfg or {}).get("student_mode", False)
    enabled = bool(env_on or yml)

    trace_dir = (cfg or {}).get("student_mode_trace_dir", "data/traces")
    note = (cfg or {}).get(
        "student_mode_note",
        "Agent is actively learning — logging traces only (no parameter updates).",
    )
    Path(trace_dir).mkdir(parents=True, exist_ok=True)
    return {"enabled": enabled, "trace_dir": trace_dir, "note": note}
