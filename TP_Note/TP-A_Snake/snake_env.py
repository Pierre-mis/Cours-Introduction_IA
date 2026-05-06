"""
Environnement Snake simplifié pour le TP-A.

Tu n'as pas à modifier ce fichier. Tu utilises l'env via :

    from snake_env import SnakeEnv
    env = SnakeEnv(grid=8, seed=42)
    state = env.reset()
    state, reward, done = env.step(action)
    env.render()                     # affichage matplotlib

État renvoyé : tuple à 5 entiers
    (danger_gauche, danger_devant, danger_droite, dir_pomme_x, dir_pomme_y)

    - danger_X ∈ {0, 1} : présence d'un mur ou de la queue dans cette direction
      relative à l'orientation courante du serpent
    - dir_pomme_x, dir_pomme_y ∈ {-1, 0, +1} : direction de la pomme dans le
      repère du serpent (avant/arrière, gauche/droite)

Actions : 0 = tourner à gauche, 1 = aller tout droit, 2 = tourner à droite.

Récompenses :
    +10  pomme mangée
    -10  mort (mur ou queue)
    -0.01 par pas (pour décourager les boucles)
"""
from collections import deque

import matplotlib.pyplot as plt
import numpy as np

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W


class SnakeEnv:
    def __init__(self, grid: int = 8, seed: int = 0):
        self.grid = grid
        self.rng = np.random.default_rng(seed)
        self.reset()

    def reset(self):
        cx, cy = self.grid // 2, self.grid // 2
        self.snake = deque([(cx, cy)])
        self.dir_idx = 1  # est
        self._place_apple()
        self.steps_since_apple = 0
        self.done = False
        return self._state()

    def _place_apple(self):
        while True:
            x = int(self.rng.integers(0, self.grid))
            y = int(self.rng.integers(0, self.grid))
            if (x, y) not in self.snake:
                self.apple = (x, y)
                return

    def _danger(self, dir_idx: int) -> int:
        head = self.snake[0]
        dx, dy = DIRS[dir_idx]
        nx, ny = head[0] + dx, head[1] + dy
        if nx < 0 or nx >= self.grid or ny < 0 or ny >= self.grid:
            return 1
        if (nx, ny) in self.snake:
            return 1
        return 0

    def _state(self):
        d_left = self._danger((self.dir_idx - 1) % 4)
        d_front = self._danger(self.dir_idx)
        d_right = self._danger((self.dir_idx + 1) % 4)
        head = self.snake[0]
        ax, ay = self.apple
        rx = int(np.sign(ax - head[0]))
        ry = int(np.sign(ay - head[1]))
        rotations = [(rx, ry), (-ry, rx), (-rx, -ry), (ry, -rx)]
        ax_rel, ay_rel = rotations[self.dir_idx]
        return (d_left, d_front, d_right, int(ax_rel), int(ay_rel))

    def step(self, action: int):
        if action == 0:
            self.dir_idx = (self.dir_idx - 1) % 4
        elif action == 2:
            self.dir_idx = (self.dir_idx + 1) % 4

        dx, dy = DIRS[self.dir_idx]
        head = self.snake[0]
        nx, ny = head[0] + dx, head[1] + dy

        if nx < 0 or nx >= self.grid or ny < 0 or ny >= self.grid or (nx, ny) in self.snake:
            self.done = True
            return self._state(), -10.0, True

        self.snake.appendleft((nx, ny))
        if (nx, ny) == self.apple:
            reward = 10.0
            self._place_apple()
            self.steps_since_apple = 0
        else:
            self.snake.pop()
            reward = -0.01
            self.steps_since_apple += 1

        if self.steps_since_apple > 100:
            self.done = True
            return self._state(), -1.0, True

        return self._state(), reward, False

    @property
    def length(self) -> int:
        return len(self.snake)

    def render(self, ax=None):
        if ax is None:
            _, ax = plt.subplots(figsize=(4, 4))
        ax.clear()
        ax.set_xlim(-0.5, self.grid - 0.5)
        ax.set_ylim(-0.5, self.grid - 0.5)
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        for j, (x, y) in enumerate(self.snake):
            color = "#2a9d8f" if j == 0 else "#264653"
            ax.add_patch(plt.Rectangle((x - 0.4, y - 0.4), 0.8, 0.8, color=color))
        ax.add_patch(plt.Rectangle((self.apple[0] - 0.4, self.apple[1] - 0.4), 0.8, 0.8, color="#e76f51"))
        ax.set_title(f"Snake — longueur {self.length}")
        return ax
