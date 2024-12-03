from algorithm.q_learning import QLearning
from algorithm.astar import AStar
import time

class HybridSolver:
    def __init__(self, maze):
        self.maze = maze
        self.q_learning = QLearning(maze)
        self.a_star = AStar(maze)

    def solve(self):
        # Start with Q-learning
        start_time = time.time()
        max_time = 1.5  # Maximum time for Q-learning in seconds
        max_episodes = 1500  # Maximum episodes for Q-learning

        print("Attempting to solve the maze using Q-learning...")
        self.q_learning.episodes = max_episodes

        try:
            q_learning_path, q_learning_length = self.q_learning.solve()
            elapsed_time = time.time() - start_time

            if elapsed_time > max_time:
                print("Q-learning exceeded time limit. Switching to A*...")
                raise TimeoutError("Q-learning took too long.")

            if not q_learning_path or q_learning_path[-1] != self.maze.end.position:
                print("Q-learning failed to find a valid solution. Switching to A*...")
                raise ValueError("Q-learning did not find a valid solution.")

            print("Q-learning successfully found a path.")
            return q_learning_path, q_learning_length

        except (TimeoutError, ValueError) as e:
            # If Q-learning fails or times out, switch to A*
            print("Attempting to solve the maze using A*...")
            a_star_path, _, a_star_length, completed = self.a_star.solve()

            if completed:
                print("A* successfully found a path.")
                return a_star_path, a_star_length
            else:
                print("A* also failed to find a valid solution.")
                return [], 0




