"""
Benchmark commun pour le TP-A — bonus "Battle the prof".

Lance 200 épisodes de Snake sur les seeds 0..199 (déterministes) avec un agent
chargé depuis un fichier .pkl. Renvoie la longueur moyenne du serpent.

Usage :
    python3 evaluate.py mon_agent.pkl
    python3 evaluate.py prof_agent.pkl
    python3 evaluate.py mon_agent.pkl prof_agent.pkl   # comparaison côte à côte

Le fichier .pkl doit contenir un dict : { state_tuple : np.array de 3 Q-values }.
Pour sauvegarder ton agent depuis Python :
    import pickle
    with open("mon_agent.pkl", "wb") as f:
        pickle.dump(Q, f)
"""
import pickle
import sys

import numpy as np

from snake_env import SnakeEnv

N_EPISODES = 200
MAX_STEPS = 500
GRID = 8


def play_one_episode(Q: dict, seed: int) -> int:
    env = SnakeEnv(grid=GRID, seed=seed)
    state = env.reset()
    steps = 0
    while not env.done and steps < MAX_STEPS:
        if state in Q:
            action = int(np.argmax(Q[state]))
        else:
            action = 1  # tout droit par défaut sur états non vus
        state, _, _ = env.step(action)
        steps += 1
    return env.length


def evaluate(path: str) -> dict:
    with open(path, "rb") as f:
        Q = pickle.load(f)

    lengths = [play_one_episode(Q, seed) for seed in range(N_EPISODES)]
    lengths = np.array(lengths)
    return {
        "path": path,
        "n_states": len(Q),
        "mean_length": float(lengths.mean()),
        "std_length": float(lengths.std()),
        "min_length": int(lengths.min()),
        "max_length": int(lengths.max()),
        "median_length": float(np.median(lengths)),
    }


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    results = [evaluate(p) for p in sys.argv[1:]]

    print(f"\nBenchmark Snake — {N_EPISODES} épisodes (seeds 0..{N_EPISODES - 1})\n")
    header = f"{'Agent':<30} {'|Q|':>8} {'longueur':>10} {'écart-type':>12} {'médiane':>10}"
    print(header)
    print("-" * len(header))
    for r in results:
        print(
            f"{r['path']:<30} {r['n_states']:>8} {r['mean_length']:>10.2f} "
            f"{r['std_length']:>12.2f} {r['median_length']:>10.1f}"
        )

    if len(results) == 2:
        diff = results[0]["mean_length"] - results[1]["mean_length"]
        print()
        if diff > 0:
            print(f"✅ {results[0]['path']} bat {results[1]['path']} de {diff:+.2f} cases.")
        elif diff < 0:
            print(f"❌ {results[0]['path']} perd contre {results[1]['path']} de {diff:.2f} cases.")
        else:
            print("⚖️  Égalité parfaite.")


if __name__ == "__main__":
    main()
