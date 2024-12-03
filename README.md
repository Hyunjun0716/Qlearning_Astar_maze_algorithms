1. Project Overview
- This project aims to develop a hybrid robot path planning solver combining Q-learning and A* algorithms. The solver is designed to efficiently navigate through complex environments by utilizing the strengths of both algorithms.
2. Project structure
- main.py: Main script to run the project.
- maze.py: Defines the classes related to the maze environment.
- q_learning.py: Implements the Q-learning algorithm.
- astar.py: Implements the A* algorithm.
- hybridsolver.py: Logic for the hybrid solver.
- README.md: Project information file.
3. Implement
- q_learning.py: Implemented the Q-learning algorithm to allow the robot to learn and navigate the maze. Defined training parameters, learning rules, and managed the exploration and learning process.
- hybridsolver.py: Developed the hybrid solver by combining Q-learning with A*, where the algorithm switches to A* when Q-learning struggles to find an optimal solution.
4. Pre-Existing Packages
- maze_solver (GitHub repository: joewong00/maze_solver)
- This package was used to facilitate maze generation and parsing functionalities. The existing code provided utility functions to create mazes of various complexities and to represent the maze as a graph structure, which was essential for implementing and testing the Q-learning and A* algorithms in this project. By leveraging this package, I was able to focus on developing and enhancing the hybrid pathfinding logic without needing to implement maze generation from scratch.