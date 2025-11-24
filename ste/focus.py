"""
focus.py – Focus Field operator.

A focus field applies a scaled inverted drift:

    m' = m + (−d · α)

This emphasizes or isolates a semantic axis encoded by d.
"""

from __future__ import annotations
import numpy as np
from numpy.typing import NDArray


def apply_focus_field(
    m: NDArray[np.floating],
    d: NDArray[np.floating],
    alpha: float = 1.0,
) -> NDArray[np.floating]:
    """
    Focus-field update:

        m' = m + (-d * alpha)

    alpha > 0 increases the strength of focus along -d.
    """
    m = np.asarray(m, dtype=np.float32)
    d = np.asarray(d, dtype=np.float32)
    return m + (-d * alpha)
