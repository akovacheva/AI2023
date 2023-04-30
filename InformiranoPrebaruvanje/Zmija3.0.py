from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search,recursive_best_first_search


class Snake(Problem):

    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal
        self.grid_size = [10, 10]

    def successor(self, state):

        # sostojba = [snake, nasoka, z_j]

        successors = dict()

        snake = state[0]
        nasoka = state[1]
        z_j = state[2]
        head = snake[0]
        head_x = head[0]
        head_y = head[1]

        tail = snake[-1]

        # ProdolzhiPravo
        if nasoka == 'jug' and (head_y - 1) >= 0:
            if (head_x, head_y - 1) in z_j:
                lista_zj = [zj for zj in z_j if zj != (head_x, head_y - 1)]
                # snake.append(tail)
                successors['ProdolzhiPravo'] = (tuple(snake), nasoka, tuple(lista_zj))
            successors['ProdolzhiPravo'] = (tuple(snake), nasoka, z_j)

        if nasoka == 'sever' and (head_y + 1) < self.grid_size[1]:
            if (head_x, head_y + 1) in z_j:
                lista_zj = [zj for zj in z_j if zj != (head_x, head_y + 1)]
                # snake.append(tail)
                successors['ProdolzhiPravo'] = (tuple(snake), nasoka, tuple(lista_zj))
            successors['ProdolzhiPravo'] = (tuple(snake), nasoka, z_j)


        if nasoka == 'istok' and (head_x + 1) < self.grid_size[0]:
            if (head_x + 1, head_y) in z_j:
                lista_zj = [zj for zj in z_j if zj != (head_x, head_y + 1)]
                # snake.append(tail)
                successors['ProdolzhiPravo'] = (tuple(snake), nasoka, tuple(lista_zj))
            successors['ProdolzhiPravo'] = (tuple(snake), nasoka, z_j)


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0

    def h(self, node):
        return 1



if __name__ == "__main__":
    n = int(input())
    zeleni_jabolki = [tuple(map(int, input().split(','))) for _ in range(n)]
    zmija = [(0, 7), (0, 8), (0, 9)]
    nasoka = 'jug'

    problem = Snake((tuple(zmija), nasoka, tuple(zeleni_jabolki)))
    print(astar_search(problem).solution())
