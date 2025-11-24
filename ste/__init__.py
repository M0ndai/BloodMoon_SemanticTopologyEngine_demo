"""
SemanticTopologyEngine (STE)

Minimal, modular framework for semantic geometry and Morphotype dynamics.
Exposes the main engine, Morphotype type and low-level operators.
"""

from .engine import SemanticTopologyEngine
from .morphotype import Morphotype
from .operators import (
    apply_drift,
    apply_coherence,
    apply_inversion,
    apply_focus_field,
)
from .artifacts import apply_artifact_noise

__all__ = [
    "SemanticTopologyEngine",
    "Morphotype",
    "apply_drift",
    "apply_coherence",
    "apply_inversion",
    "apply_focus_field",
    "apply_artifact_noise",
]
