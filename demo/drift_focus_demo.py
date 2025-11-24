"""
drift_focus_demo.py – Demo für Drift + Focus Field.

Entspricht konzeptionell dem Beispiel aus deinem README:

- Start mit einem Morphotype
- Erzeuge einen Drift d
- Zieh m entlang d (Deformation)
- Wende danach einen Focus-Field-Schritt entlang -d an
"""

from __future__ import annotations
import numpy as np

from drift import apply_drift
from focus import apply_focus_field
from inversion import invert_drift


def main() -> None:
    dim = 32
    rng = np.random.default_rng(7)

    # initial morphotype
    m = rng.normal(0.0, 0.1, size=(dim,)).astype(np.float32)
    print("Initial morphotype (m):")
    print(m)

    # define a drift as simple scaled copy of m
    d = m * 0.1
    print("\nDrift vector (d = 0.1 * m):")
    print(d)

    # apply drift: m1 = m + d
    m1 = apply_drift(m, d)
    print("\nAfter drift (m1 = m + d):")
    print(m1)

    # focus field via inverted drift
    d_inv = invert_drift(d)
    m2 = apply_focus_field(m1, d_inv, alpha=1.0)
    print("\nAfter focus field (m2 = m1 + (-d) * alpha):")
    print(m2)


if __name__ == "__main__":
    main()
