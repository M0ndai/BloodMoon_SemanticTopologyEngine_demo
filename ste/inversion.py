"""
inversion.py – Inversion operator for drift vectors.

Inversion negates a drift vector:

    inv(d) = −d

Useful for counter-aligned semantic analysis and focus fields.
"""

from __future__ import annotations
import numpy as np
from numpy.typing import NDArray


def invert_drift(d: NDArray[np.floating]) -> NDArray[np.floating]:
    """
    Return inverted drift:

        inv(d) = -d
    """
    d = np.asarray(d, dtype=np.float32)
    return -d
