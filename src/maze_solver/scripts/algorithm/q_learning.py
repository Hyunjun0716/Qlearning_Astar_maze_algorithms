import numpy as np
import random

class QLearning:
    def __init__(self, maze, alpha=0.1, gamma=0.9, epsilon=1.0, epsilon_decay=0.99, min_epsilon=0.1, episodes=1500):
        self.maze = maze  
        self.alpha = alpha  # Learning rate: controls how much the Q-value is updated
        self.gamma = gamma  # Discount factor: determines the importance of future rewards
        self.epsilon = epsilon  
        self.epsilon_decay = epsilon_decay  
        self.min_epsilon = min_epsilon  
        self.episodes = episodes  
        self.q_table = {} 
        self.init_q_table()  # Initialize Q-table

    def init_q_table(self):
        # Initialize the Q-table with zeros for all actions in each state
        for node in self.maze.nodes():
            self.q_table[node.position] = [0, 0, 0, 0]  # Actions: [up, right, down, left]

    def choose_action(self, state):
        # Choose an action based on epsilon-greedy policy
        if random.uniform(0, 1) < self.epsilon:
            return random.choice([0, 1, 2, 3])  
        return np.argmax(self.q_table[state])  # Best action based on Q-table (exploitation)

    def update_q_value(self, state, action, reward, next_state):
        # Update the Q-value using the Q-learning formula
        old_value = self.q_table[state][action]  # Current Q-value for the state-action pair
        next_max = max(self.q_table[next_state]) if next_state in self.q_table else 0  # Max Q-value for next state
        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)  # Updated Q-value
        self.q_table[state][action] = new_value  # Update Q-table

    def solve(self):
        # Train the Q-learning agent over multiple episodes
        for episode in range(self.episodes):
            state = self.maze.start.position  # Start state
            total_reward = 0  # Total reward for the episode
            steps = 0  # Number of steps in the episode

            print(f"Episode {episode + 1}/{self.episodes} started.")
            while state != self.maze.end.position:  # Continue until the goal is reached
                action = self.choose_action(state)  
                next_state, reward = self.take_action(state, action)  # Perform the action
                self.update_q_value(state, action, reward, next_state)  
                state = next_state  
                total_reward += reward  # Accumulate reward
                steps += 1  # Increment step count

                if state == self.maze.end.position:  # Goal is reached
                    print(f"Goal reached in episode {episode + 1} after {steps} steps.")
                    break

            self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay)  # Decay epsilon
            print(f"Episode {episode + 1} finished: Total Reward = {total_reward}, Steps = {steps}")
            print("-" * 50)

        print("Training completed. Extracting optimal path...")
        return self.extract_path()  # Extract the optimal path after training

    def take_action(self, state, action):
        # Perform an action in the maze and return the resulting state and reward
        node = self.maze.get_node(state)  # Get the current node
        next_node = node.neighbours[action] if node and action < len(node.neighbours) else None  # Get the next node
        if next_node:
            return next_node.position, -1  # Small penalty for moving
        return state, -10  # Large penalty for hitting a wall

    def extract_path(self):
        # Extract the optimal path from the Q-table after training
        path = []  # List to store the optimal path
        state = self.maze.start.position  # Start state
        while state != self.maze.end.position:  # Continue until the goal is reached
            path.append(state)  # Add the current state to the path
            action = np.argmax(self.q_table[state])  # Choose the best action based on Q-values
            node = self.maze.get_node(state)  # Get the current node
            next_node = node.neighbours[action] if node else None  # Get the next node
            if next_node:
                state = next_node.position  # Move to the next state
            else:
                break  # Stop if no valid next node
        path.append(self.maze.end.position)  # Add the goal state to the path
        return path, len(path)  # Return the optimal path and its length