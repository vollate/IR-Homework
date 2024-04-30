import numpy as np
import random


class GridWorldMC:
    def __init__(self, size=3, alpha=0.5, gamma=0.9):
        self.size = size
        self.q_values = np.zeros((size, size, 4))
        self.returns = {}
        self.policy = np.zeros((size, size, 4)) + 0.25
        self.terminal_state = (0, 2)
        self.gamma = gamma
        self.action_dict = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
        self.alpha = alpha
        for i in range(size):
            for j in range(size):
                for a in range(4):
                    self.returns[(i, j, a)] = []

    def generate_episode(self):
        episode = []
        state = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
        while state != self.terminal_state:
            action_probs = self.policy[state]
            action = np.random.choice(np.arange(len(action_probs)), p=action_probs)
            next_state = (max(min(state[0] + self.action_dict[action][0], self.size - 1), 0),
                          max(min(state[1] + self.action_dict[action][1], self.size - 1), 0))
            reward = -1 if next_state != self.terminal_state else 0
            episode.append((state, action, reward))
            state = next_state
        return episode

    def generate_episode2(self):
        episode = []
        state = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
        while state != self.terminal_state:
            action_probs = self.policy[state]
            action = np.random.choice(np.arange(len(action_probs)), p=action_probs)
            next_state = (max(min(state[0] + self.action_dict[action][0], self.size - 1), 0),
                          max(min(state[1] + self.action_dict[action][1], self.size - 1), 0))
            if next_state == (1, 1):
                reward = -1
            else:
                reward = -0.1
            episode.append((state, action, reward))
            state = next_state
        return episode

    def mc_control_es(self, episodes):
        paths = []
        for e in range(episodes):
            episode = self.generate_episode2()
            paths.append([s for s, a, r in episode])
            G = 0
            for t in range(len(episode) - 1, -1, -1):
                state, action, reward = episode[t]
                G = self.gamma * G + reward
                if not (state, action) in [(x[0], x[1]) for x in episode[0:t]]:
                    self.returns[(state + (action,))].append(G)
                    self.q_values[state[0], state[1], action] = np.mean(self.returns[(state + (action,))])
                    # Removed policy update
        return paths

    def generate_episode_sarsa(self):
        episode = []
        state = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
        step = 0
        while state != self.terminal_state and step < 5:
            action_probs = self.policy[state]
            action = np.random.choice(np.arange(len(action_probs)), p=action_probs)
            next_state = (max(min(state[0] + self.action_dict[action][0], self.size - 1), 0),
                          max(min(state[1] + self.action_dict[action][1], self.size - 1), 0))
            # if next_state == (1, 1):
            #     reward = -1
            # else:
            reward = -1
            episode.append((state, action, reward))
            state = next_state
            step += 1
        return episode

    def sarsa(self, episodes):
        paths = []
        for e in range(episodes):
            episode = self.generate_episode_sarsa()
            paths.append([s for s, a, r in episode])  # Append states to paths
            G = 0
            for t in range(len(episode) - 1):
                state, action, reward = episode[t]
                next_state, next_action, _ = episode[t + 1]
                G = self.gamma * G + reward
                self.q_values[state[0], state[1], action] += self.alpha * (
                        reward + self.gamma * self.q_values[next_state[0], next_state[1], next_action] -
                        self.q_values[state[0], state[1], action])
        return paths

    def q_learning(self, episodes):
        paths = []
        for e in range(episodes):
            episode = self.generate_episode_sarsa()
            paths.append([s for s, a, r in episode])  # Append states to paths
            G = 0
            for t in range(len(episode) - 1):
                state, action, reward = episode[t]
                next_state, _, _ = episode[t + 1]
                G = self.gamma * G + reward
                # Choose next action based on max Q-value of next state
                next_action = np.argmax(self.q_values[next_state[0], next_state[1]])
                self.q_values[state[0], state[1], action] += self.alpha * (
                        reward + self.gamma * self.q_values[next_state[0], next_state[1], next_action] -
                        self.q_values[state[0], state[1], action])
        return paths

    def print_q_table_markdown(self):
        # Print table header
        print("| State | Up | Down | Left | Right |")
        print("|-------|----|------|------|-------|")
        for i in range(self.size):
            for j in range(self.size):
                print(f"| ({i},{j}) |", end=" ")
                for a in range(4):
                    print(f"{self.q_values[i, j, a]:.2f} |", end=" ")
                print()


grid_world_mc = GridWorldMC()

for i in range(1, 5):
    print(f"Episode {i}:")
    paths = grid_world_mc.q_learning(1)

    # Print paths
    print("Visited States:")
    for path in paths:
        print(" -> ".join(str(s) for s in path), end="")
    # print(" -> (0,2)")
    # Print Q-table in Markdown
    print("\nQ-table in Markdown:")
    grid_world_mc.print_q_table_markdown()

    print("\n")
