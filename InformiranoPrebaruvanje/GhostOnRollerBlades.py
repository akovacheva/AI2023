from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search

class GhostOnSkates(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.width = n
        self.height = n
        self.grid_size = (n,n)


    def successor(self, state):
        successors = dict()
        # (x,y) - pozicija na ghost
        ghost_x = state[0]
        ghost_y = state[1]

        ghost_x, ghost_y = state
        if ghost_y + 3 < self.height and (ghost_x, ghost_y + 3) not in holes:
            successors["Gore 3"] = (ghost_x, ghost_y + 3)
        if ghost_x + 3 < self.width and (ghost_x + 3, ghost_y) not in holes:
            successors["Desno 3"] = (ghost_x + 3, ghost_y)

        if "Gore 3" not in successors and "Desno 3" not in successors:
            if ghost_y + 2 < self.height and (ghost_x, ghost_y + 2) not in holes:
                successors["Gore 2"] = (ghost_x, ghost_y + 2)
            if ghost_x + 2 < self.width and (ghost_x + 2, ghost_y) not in holes:
                successors["Desno 2"] = (ghost_x + 2, ghost_y)

            if "Gore 2" not in successors and "Desno 2" not in successors:
                if ghost_y + 1 < self.height and (ghost_x, ghost_y + 1) not in holes:
                    successors["Gore 1"] = (ghost_x, ghost_y + 1)
                if ghost_x + 1 < self.width and (ghost_x + 1, ghost_y) not in holes:
                    successors["Desno 1"] = (ghost_x + 1, ghost_y)

        # #Gore
        # if ghost_y + 1 < self.height and (ghost_x, ghost_y + 1) not in holes:
        #     successors["Gore 1"] = (ghost_x, ghost_y + 1)
        # elif ghost_y + 1 < self.height and (ghost_x, ghost_y + 1) in holes:
        #     successors["Gore 2"] = (ghost_x, ghost_y + 2)
        # elif ghost_y + 2 < self.height and (ghost_x, ghost_y + 2) not in holes:
        #     successors["Gore 2"] = (ghost_x, ghost_y + 2)
        # elif ghost_y + 2 < self.height and (ghost_x, ghost_y + 2) in holes:
        #     successors["Gore 3"] = (ghost_x, ghost_y + 3)
        # elif ghost_y + 3 < self.height and (ghost_x, ghost_y + 3) not in holes:
        #     successors["Gore 3"] = (ghost_x, ghost_y + 3)
        #
        # #Desno
        # if ghost_x + 1 < self.width and (ghost_x + 1, ghost_y) not in holes :
        #     successors["Desno 1"]= (ghost_x + 1, ghost_y)
        # elif ghost_x + 1 < self.width and (ghost_x + 1, ghost_y)  in holes:
        #     successors["Desno 2"] = (ghost_x + 2, ghost_y)
        # elif ghost_x + 2 < self.width and (ghost_x + 2, ghost_y) not in holes:
        #     successors["Desno 2"] = (ghost_x + 2, ghost_y)
        # elif ghost_x + 2 < self.width and (ghost_x + 2, ghost_y) in holes:
        #     successors["Desno 3"] = (ghost_x + 3, ghost_y)
        # elif ghost_x + 3 < self.width and (ghost_x + 3, ghost_y) in holes:
        #     successors["Desno 3"] = (ghost_x + 3, ghost_y)



        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]
    def h(self, node):
        #menheten rastojanie megju pozicija na duhot i pacman

        x_ghost = node.state[0]
        y_ghost = node.state[1]
        x_pacman = self.goal[0]
        y_pacman = self.goal[1]

        return abs(x_ghost-x_pacman) + abs(y_ghost-y_pacman)


if __name__ == '__main__':
    n = int(input())
    ghost_pos = (0, 0)
    goal_pos = (n - 1, n - 1)
    num_holes = int(input())
    holes = list()
    for _ in range(num_holes):
        holes.append(tuple(map(int, input().split(','))))

    problem = GhostOnSkates(ghost_pos, goal_pos)
    answer = recursive_best_first_search(problem)
    print(answer.solution())