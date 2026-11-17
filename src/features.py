import math
import numpy as np

COMPARATIVE_CUES = [
    "outperforms", "improves upon", "new state of the art", "state-of-the-art",
    "limitations of previous", "surpasses", "replaces", "superseded"
]

def compute_temporal_risk(pub_year: int, eval_year: int = 2026, tau_age: float = 12.0) -> float:
    age = max(0, int(eval_year) - int(pub_year))
    return round(min(1.0, age / tau_age), 4)

def compute_foundational_velocity(cited_by_count: int, age: int) -> float:
    val = math.log(1.0 + max(0, cited_by_count)) / (5.5 * math.log(2.0 + max(0, age)))
    return round(min(1.0, val), 4)

def compute_lexical_supersession(candidate_abstracts: list) -> float:
    hits = 0
    for abs_text in candidate_abstracts:
        low = abs_text.lower()
        if any(cue in low for cue in COMPARATIVE_CUES):
            hits += 1
    return round(min(1.0, hits / 3.0), 4)

def compute_hybrid_supersession(s_lex: np.ndarray, s_nli: np.ndarray, intent: np.ndarray) -> np.ndarray:
    return np.where(intent > 0.50, np.maximum(s_lex, s_nli), 0.25 * s_lex)
