from ste.engine import SemanticTopologyEngine
import numpy as np

def main():
    ste = SemanticTopologyEngine(dim=32)

    ste.register("sample")
    m = ste["sample"]

    drift = m.morphotype * 0.1
    ste.drift(m, drift)

    focus = ste.invert(drift)
    ste.focus(m, focus, alpha=1.0)

    print("Final vector:")
    print(m.morphotype)

if __name__ == "__main__":
    main()
