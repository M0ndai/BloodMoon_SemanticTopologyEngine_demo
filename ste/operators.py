import numpy as np


# ----------------------
# Drift
# ----------------------
def apply_drift(m, drift):
    """
    Basic linear deformation: m' = m + d
    """
    return m + drift


# ----------------------
# Coherence
# ----------------------
def apply_coherence(m, drift, lam):
    """
    Coherence relaxation: m' = m - lam * d
    """
    return m - lam * drift


# ----------------------
# Inversion
# ----------------------
def apply_inversion(d):
    """
    Inversion: inv(d) = -d
    """
    return -d


# ----------------------
# Focus Field
# ----------------------
def apply_focus_field(m, drift, alpha):
    """
    Focus field: m' = m + (-d * alpha)
    """
    return m + (-drift * alpha)
