"""
drift.py – Drift operator for the SemanticTopologyEngine (STE).

Drift represents directed semantic displacement:

    d = m(t+1) − m(t)

In practice we often apply a drift vector d to a current morphotype m:

    m' = m + d

This module keeps it deliberately minimal and NumPy-based.
"""

from __future__ import annotations
import numpy as np
from numpy.typing import NDArray


def compute_drift(m_t: NDArray[np.floating], m_t1: NDArray[np.floating]) -> NDArray[np.floating]:
    """
    Compute drift vector d between two morphotype states.

    d = m(t+1) - m(t)
    """
    m_t = np.asarray(m_t, dtype=np.float32)
    m_t1 = np.asarray(m_t1, dtype=np.float32)
    return m_t1 - m_t


def apply_drift(m: NDArray[np.floating], d: NDArray[np.floating]) -> NDArray[np.floating]:
    """
    Apply a drift vector d to current morphotype m:

        m' = m + d
    """
    m = np.asarray(m, dtype=np.float32)
    d = np.asarray(d, dtype=np.float32)
    return m + d
