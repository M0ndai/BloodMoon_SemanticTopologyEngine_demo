import numpy as np


def apply_artifact_noise(m, cfg):
    """
    Structured noise generation for perturbation & robustness testing.
    """

    mode = cfg.get("mode", "distributed_noise")
    gain = cfg.get("mutation_gain", 0.1)
    entropy_bias = cfg.get("entropy_bias", 0.0)
    coherence_penalty = cfg.get("coherence_penalty", 0.0)

    if mode == "distributed_noise":
        noise = np.random.normal(entropy_bias, gain, size=m.shape)
        m2 = m + noise + coherence_penalty
        return m2.astype(np.float32)

    # Fallback = no modification
    return m
