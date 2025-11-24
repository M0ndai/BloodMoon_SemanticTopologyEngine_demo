import numpy as np

from ste.morphotype import Morphotype


def test_morphotype_initialization_and_property():
    vec = np.array([1.0, -2.0, 3.5], dtype=np.float32)
    m = Morphotype(name="test", vector=vec)

    assert m.name == "test"
    np.testing.assert_allclose(m.vector, vec)
    # property alias
    np.testing.assert_allclose(m.morphotype, vec)


def test_morphotype_stretch_adds_drift():
    vec = np.array([0.0, 1.0, 2.0], dtype=np.float32)
    drift = np.array([0.5, -0.5, 1.0], dtype=np.float32)

    m = Morphotype(name="test", vector=vec.copy())
    m.stretch(drift)

    expected = vec + drift
    np.testing.assert_allclose(m.vector, expected, rtol=1e-6, atol=1e-6)
