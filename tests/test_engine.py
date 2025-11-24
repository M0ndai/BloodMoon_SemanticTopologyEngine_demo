import numpy as np
import pytest

from ste import (
    SemanticTopologyEngine,
    apply_drift,
    apply_coherence,
    apply_inversion,
    apply_focus_field,
)


def test_register_and_getitem():
    ste = SemanticTopologyEngine(dim=8)
    m = ste.register("sample")

    assert "sample" in ste._store  # internal registry
    assert m is ste["sample"]
    assert m.vector.shape == (8,)
    assert m.vector.dtype == np.float32


def test_drift_operator_mutates_morphotype():
    ste = SemanticTopologyEngine(dim=4)
    m = ste.register("sample", init=np.zeros(4, dtype=np.float32))

    drift_vec = np.array([1.0, -1.0, 0.5, 0.0], dtype=np.float32)
    ste.drift(m, drift_vec)

    expected = drift_vec
    np.testing.assert_allclose(m.vector, expected, rtol=1e-6, atol=1e-6)


def test_coherence_operator_moves_against_drift():
    ste = SemanticTopologyEngine(dim=3)
    init = np.array([1.0, 2.0, 3.0], dtype=np.float32)
    m = ste.register("sample", init=init)

    drift_vec = np.array([0.5, -0.5, 1.0], dtype=np.float32)
    lam = 0.2

    # pure coherence (without drift application beforehand)
    ste.coherence(m, drift_vec, lam=lam)

    expected = init - lam * drift_vec
    np.testing.assert_allclose(m.vector, expected, rtol=1e-6, atol=1e-6)


def test_invert_returns_negative_vector():
    ste = SemanticTopologyEngine(dim=3)
    d = np.array([0.3, -1.2, 5.0], dtype=np.float32)

    inv = ste.invert(d)
    np.testing.assert_allclose(inv, -d, rtol=1e-6, atol=1e-6)


def test_focus_field_uses_inverted_drift_and_alpha():
    ste = SemanticTopologyEngine(dim=3)
    init = np.array([1.0, 0.0, -1.0], dtype=np.float32)
    m = ste.register("sample", init=init)

    drift_vec = np.array([0.5, 0.5, -0.5], dtype=np.float32)
    alpha = 2.0

    # m' = m + (-d * alpha)
    ste.focus(m, drift_vec, alpha=alpha)

    expected = init + (-drift_vec * alpha)
    np.testing.assert_allclose(m.vector, expected, rtol=1e-6, atol=1e-6)


def test_artifacts_preserve_shape_and_type():
    ste = SemanticTopologyEngine(dim=5)
    init = np.zeros(5, dtype=np.float32)
    m = ste.register("sample", init=init)

    cfg = {
        "mode": "distributed_noise",
        "entropy_bias": 0.12,
        "mutation_gain": 0.30,
        "coherence_penalty": -0.05,
    }

    # fix RNG for reproducibility if artifacts implementation uses np.random
    np.random.seed(42)
    ste.artifacts(m, cfg)

    assert m.vector.shape == init.shape
    assert m.vector.dtype == np.float32
    # sehr unwahrscheinlich, dass das exakt alles Nullen bleibt
    assert not np.allclose(m.vector, init)
