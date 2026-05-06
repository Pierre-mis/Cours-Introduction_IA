"""
Visualisation en direct d'un agent qui joue à Snake.

Ouvre une fenêtre matplotlib qui montre l'agent jouant en boucle. Ferme la
fenêtre pour quitter.

Usage :
    python3 play_live.py prof_agent.pkl
    python3 play_live.py mon_agent.pkl --fps 10
    python3 play_live.py mon_agent.pkl --seed 0   # seed de départ fixé
"""
import argparse
import pickle
import time

import matplotlib.pyplot as plt
import numpy as np

from snake_env import SnakeEnv

GRID = 8
MAX_STEPS = 500


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("agent", help="Chemin vers le .pkl de la Q-table")
    parser.add_argument("--fps", type=int, default=8, help="Vitesse d'affichage (cases/s)")
    parser.add_argument("--seed", type=int, default=None, help="Graine fixe (sinon aléatoire)")
    args = parser.parse_args()

    with open(args.agent, "rb") as f:
        Q = pickle.load(f)
    print(f"Agent chargé : {args.agent} ({len(Q)} états)")

    fig, ax = plt.subplots(figsize=(5, 5.5))
    fig.canvas.manager.set_window_title(f"Snake — {args.agent}")

    rng = np.random.default_rng(args.seed)
    episode = 0
    total_apples = 0
    best_length = 0

    plt.ion()
    plt.show(block=False)

    delay = 1.0 / args.fps

    try:
        while plt.fignum_exists(fig.number):
            episode += 1
            seed = args.seed if args.seed is not None else int(rng.integers(0, 1_000_000))
            env = SnakeEnv(grid=GRID, seed=seed)
            state = env.reset()
            steps = 0

            while not env.done and steps < MAX_STEPS and plt.fignum_exists(fig.number):
                action = int(np.argmax(Q[state])) if state in Q else 1
                state, _, _ = env.step(action)
                steps += 1

                env.render(ax=ax)
                ax.set_title(
                    f"Épisode {episode} · longueur {env.length} · "
                    f"meilleure {best_length} · pommes totales {total_apples}"
                )
                fig.canvas.draw_idle()
                fig.canvas.flush_events()
                time.sleep(delay)

            apples_this_ep = env.length - 1
            total_apples += apples_this_ep
            best_length = max(best_length, env.length)
            print(
                f"Épisode {episode} : longueur {env.length} ({apples_this_ep} pommes), "
                f"meilleur jusqu'ici {best_length}"
            )
            if plt.fignum_exists(fig.number):
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nInterrompu.")


if __name__ == "__main__":
    main()
