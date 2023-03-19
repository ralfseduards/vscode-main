import sys

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.action = action
        self.parent = parent
        #+ path cost


class StackFrontier:
    """implements the idea of a frontier"""
    def __init__(self, ):
        self.frontier = []

    # allows adding
    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state): 
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    # allows removing
    def remove(self, node):
        if len(self.frontier) == 0:
            raise Exception("frontier is empty")
        else:
            # because the structure is a stack it removes the last node
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):
    """for use with queues (breadth-first search)"""
    def __init__(self):
        super(self).__init__()

    def remove(self,node):
        if len(self.frontier) == 0:
            raise Exception("the queue is empty")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node 

class Maze:
    """takes a text like maze from a file"""
    def __init__(self, filename):
        # read the file and set height and width of the maze
        with open(filename) as f:
            contents = f.read()

        # validate start and end points
        if contents.count("A") != 1:
            raise Exception("file must have 1 starting point")
        if contents.count("B") != 1:
            raise Exception(("file must have 1 ending point"))

        # determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i,j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.end = (i,j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        self.solution = None


        def print(self):
            solution = self.solution[1] if self.solution is not None else None
            print()
            for i, row in enumerate(self.walls):
                for j, col in enumerate(row):
                    if col:
                        print("∑" , end = "")
                    elif (i,j) == self.start:
                        print("A" , end = "")
                    elif solution is not None and (i,j) is solution:
                        print("*" , end = "")
                    else:
                        print(" ", end = "")
                print()
            print()

        def neighbors(self,state):
            row, col = state

            # all possible actions
            candidates =[
                ("up", (row - 1 , col)),
                ("down", (row + 1, col)),
                ("left", (row, col - 1)),
                ("right", (row, col + 1))
            ]

            # ensure actions are valid
            result = []
            for action, (r,c) in candidates:
                try:
                    if not self.walls[r][c]:
                        result.append((action, (r,c)))
                except IndexError:
                    continue
            return result

class Solve(self):
    """finds a solutions to a maze, if a maze exists"""

    # keeps track of states explored
    self.num_explored = 0

    # initialize frontier for the starting position
    start = Node(state = self.start, parent = None, action= None)
    frontier = StackFrontier()
    frontier.add(start)

    # init an empty explored set
    self.explored = set()

    # keep looping until solution is found
    while True:

        # if nothing left in frontier, the no path
        if frontier.empty():
            raise Exception("no solution")

        # choose a node from the frontier
        node = frontier.remove()
        self.num_explored += 1

        # if node is the goal then we have our solution
        if node.state == self.goal:
            actions = []
            cells = []

            # then look for the steps to solution by going back using parents
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent 
            # have to reverse
            actions.reverse()
            cells.reverse()
            self.solution = (actions, cells)
            return

        # mark node as explored
        self.explored.add(node.state)

        for action, state in self.neighbors(node.state):
            if not frontier.contains_state(state) and state not in self.explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)

            