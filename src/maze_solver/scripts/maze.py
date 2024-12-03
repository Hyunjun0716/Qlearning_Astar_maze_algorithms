import numpy as np

class Maze:
    class Node:
        def __init__(self, position=None):
            self.position = position
            self.neighbours = [None, None, None, None]  # [up, right, down, left]

        def __lt__(self, other):
            return self.position < other.position

        def __gt__(self, other):
            return self.position > other.position

    def __init__(self, arr):
        maze = np.array(arr)
        self.width = maze.shape[0]
        self.height = maze.shape[1]
        self.start = None
        self.end = None
        self.nodecount = 0
        self.nodes_list = []

        # Initialize the maze and its nodes
        toprownodes = [None] * self.width

        # Starting node
        for y in range(self.height):
            if maze[0, y] == 0:
                self.start = Maze.Node((0, y))
                toprownodes[y] = self.start
                self.nodes_list.append(self.start)
                self.nodecount += 1

        # Intermediate nodes
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                if maze[x, y] == 0:
                    n = Maze.Node((x, y))
                    self.nodes_list.append(n)
                    self.nodecount += 1

                    # Connect nodes
                    if maze[x - 1, y] == 0:  # Up
                        t = toprownodes[y]
                        t.neighbours[2] = n
                        n.neighbours[0] = t
                    if maze[x + 1, y] == 0:  # Down
                        toprownodes[y] = n
                    else:
                        toprownodes[y] = None
                    if maze[x, y - 1] == 0:  # Left
                        n.neighbours[3] = self.get_node((x, y - 1))
                        self.get_node((x, y - 1)).neighbours[1] = n

        # Ending node
        for y in range(self.height):
            if maze[-1, y] == 0:
                self.end = Maze.Node((self.height - 1, y))
                t = toprownodes[y]
                if t:
                    t.neighbours[2] = self.end
                    self.end.neighbours[0] = t
                self.nodes_list.append(self.end)
                self.nodecount += 1
                break

    def nodes(self):
        return self.nodes_list

    def get_node(self, position):
        for node in self.nodes_list:
            if node.position == position:
                return node
        return None

                
