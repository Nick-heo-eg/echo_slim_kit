"""Tiny, self-contained 'judgment loop' to illustrate structure.

This is NOT your production Echo Judgment System.
It just shows the idea of:
  - input capsule
  - run judgment
  - emit decision + trace
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class JudgmentInput:
    text: str
    intent: str = "demo"


@dataclass
class JudgmentResult:
    decision: str
    confidence: float
    reasoning: str


def run_judgment(input_: JudgmentInput) -> JudgmentResult:
    # toy heuristic
    score = 0.9 if "risk" in input_.text.lower() else 0.7
    decision = "approve" if score >= 0.8 else "review"
    reasoning = f"toy-heuristic: score={score:.2f}, decision={decision}"
    return JudgmentResult(decision=decision, confidence=score, reasoning=reasoning)


def run_judgment_with_trace(payload: Dict[str, Any]) -> Dict[str, Any]:
    input_ = JudgmentInput(text=payload.get("text", ""), intent=payload.get("intent", "demo"))
    result = run_judgment(input_)
    return {
        "input": asdict(input_),
        "result": asdict(result),
        "trace_signature": {
            "mode": "SLIM_JUDGMENT_LOOP",
            "clarity": "demo",
            "resonance": "stub",
        },
    }
