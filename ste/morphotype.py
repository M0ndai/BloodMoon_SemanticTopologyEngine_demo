import numpy as np


class Morphotype:
    """
    A Morphotype is a high-dimensional semantic vector that can undergo
    deformation, inversion, focus-field operations, and structured noise injection.
    """

    def __init__(self, name: str, vector: np.ndarray):
        self.name = name
        self.vector = vector.astype(np.float32)

    @property
    def morphotype(self):
        return self.vector

    # Generic stretch / deformation
    def stretch(self, drift_vec):
        self.vector = self.vector + drift_vec
