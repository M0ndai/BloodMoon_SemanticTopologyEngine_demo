"""
coherence.py – Coherence relaxation for Morphotypes.

Coherence reduces displacement magnitude and stabilizes Morphotypes:

    m' = m − λ d

where:
    m  = current morphotype vector
    d  = drift vector
    λ  = coherence factor in [0, ∞) (typically small, e.g. 0.05–0.3)
"""

from __future__ import annotations
import numpy as np
from numpy.typing import NDArray


def apply_coherence(
    m: NDArray[np.floating],
    d: NDArray[np.floating],
    lam: float = 0.1,
) -> NDArray[np.floating]:
    """
    Coherence relaxation:

        m' = m - lam * d

    lam > 0 pulls the morphotype back against the drift,
    suppressing excessive dispersion.
    """
    m = np.asarray(m, dtype=np.float32)
    d = np.asarray(d, dtype=np.float32)
    return m - lam * d
