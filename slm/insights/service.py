from dataclasses import dataclass
from typing import Dict, Any
import time

@dataclass
class InsightsSummary:
    agent_id: str
    ts: float
    steps: int
    avg_reward_1h: float
    loss_ema: float
    memory_hit_rate: float

    def to_dict(self) -> Dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "ts": self.ts,
            "steps": self.steps,
            "avg_reward_1h": self.avg_reward_1h,
            "loss_ema": self.loss_ema,
            "memory_hit_rate": self.memory_hit_rate,
        }

def get_insights_summary(agent_id: str) -> Dict[str, Any]:
    # TODO: wire to real tracer metrics
    return InsightsSummary(
        agent_id=agent_id,
        ts=time.time(),
        steps=0,
        avg_reward_1h=0.0,
        loss_ema=0.0,
        memory_hit_rate=0.0,
    ).to_dict()
