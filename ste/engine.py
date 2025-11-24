import numpy as np
from .morphotype import Morphotype
from .operators import (
    apply_drift,
    apply_coherence,
    apply_inversion,
    apply_focus_field
)
from .artifacts import apply_artifact_noise


class SemanticTopologyEngine:
    """
    Core engine for managing Morphotypes and applying semantic topology operators.
    """

    def __init__(self, dim=32):
        self.dim = dim
        self._store = {}

    # ----------------------------------------------------
    # Registry
    # ----------------------------------------------------
    def register(self, name, init=None):
        if init is None:
            init = np.random.normal(0, 0.1, self.dim)

        self._store[name] = Morphotype(name=name, vector=init.astype(np.float32))
        return self._store[name]

    def __getitem__(self, name):
        return self._store[name]

    # ----------------------------------------------------
    # Operators
    # ----------------------------------------------------
    def drift(self, m: Morphotype, drift_vec):
        m.vector = apply_drift(m.vector, drift_vec)

    def coherence(self, m: Morphotype, drift_vec, lam=0.1):
        m.vector = apply_coherence(m.vector, drift_vec, lam)

    def invert(self, drift_vec):
        return apply_inversion(drift_vec)

    def focus(self, m: Morphotype, drift_vec, alpha=1.0):
        m.vector = apply_focus_field(m.vector, drift_vec, alpha)

    def artifacts(self, m: Morphotype, cfg: dict):
        m.vector = apply_artifact_noise(m.vector, cfg)

    # ----------------------------------------------------
    # Convenience
    # ----------------------------------------------------
    def summary(self):
        return {
            name: mt.vector.tolist()
            for name, mt in self._store.items()
        }
