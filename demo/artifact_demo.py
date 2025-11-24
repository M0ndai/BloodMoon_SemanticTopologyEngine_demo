"""
artifact_demo.py – Demo for structured noise / "Artifacts" in STE.

This does *not* depend auf einer großen Engine.
Es zeigt nur:

- Erzeugen eines Morphotype-Vektors
- Konfigurieren eines Artifact-"Noise"-Profils
- Anwenden der Störung
"""

from __future__ import annotations
import numpy as np


def apply_artifact_noise(
    m: np.ndarray,
    mode: str = "distributed_noise",
    entropy_bias: float = 0.12,
    mutation_gain: float = 0.30,
    coherence_penalty: float = -0.05,
) -> np.ndarray:
    """
    Structured noise (Artifact) for robustness/diversification studies.

    mode="distributed_noise":
        Draws Gaussian noise around entropy_bias with std=mutation_gain
        and adds a global coherence_penalty.
    """
    m = np.asarray(m, dtype=np.float32)

    if mode == "distributed_noise":
        noise = np.random.normal(loc=entropy_bias, scale=mutation_gain, size=m.shape)
        return (m + noise + coherence_penalty).astype(np.float32)

    # fallback – no change
    return m


def main() -> None:
    dim = 16
    rng = np.random.default_rng(42)

    # initial morphotype
    m = rng.normal(0.0, 0.1, size=(dim,)).astype(np.float32)
    print("Initial morphotype:")
    print(m)

    artifact_cfg = {
        "mode": "distributed_noise",
        "entropy_bias": 0.12,
        "mutation_gain": 0.30,
        "coherence_penalty": -0.05,
    }

    m_art = apply_artifact_noise(
        m,
        mode=artifact_cfg["mode"],
        entropy_bias=artifact_cfg["entropy_bias"],
        mutation_gain=artifact_cfg["mutation_gain"],
        coherence_penalty=artifact_cfg["coherence_penalty"],
    )

    print("\nMorphotype after artifact noise:")
    print(m_art)


if __name__ == "__main__":
    main()
