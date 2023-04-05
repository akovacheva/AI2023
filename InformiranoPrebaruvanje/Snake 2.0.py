from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search,recursive_best_first_search

def gore(snake, zeleni):

    head = snake[1]
    head_x = head[0]
    head_y = head[1]

    if head_y + 1 < 10 and (head_x,head_y + 1) not in snake:
        new_head = (head_x,head_y + 1)
        if new_head in zeleni:
            zeleni.remove(new_head)
            snake.append(new_head)
        else:
            snake = snake[1:]
            snake.append(new_head)

    return tuple(snake), tuple(zeleni)

def dolu(snake, zeleni):

    head = snake[-1]
    head_x = head[0]
    head_y = head[1]

    if head_y - 1 >= 0 and (head_x,head_y - 1) not in snake:
        new_head = (head_x,head_y - 1)
        if new_head in zeleni:
            zeleni.remove(new_head)
            snake.append(new_head)
        else:
            snake = snake[1:]
            snake.append(new_head)

    return tuple(snake), tuple(zeleni)

def desno(snake, zeleni):

    head = snake[-1]
    head_x = head[0]
    head_y = head[1]

    if head_x + 1 < 10 and (head_x + 1,head_y) not in snake:
        new_head = (head_x + 1,head_y)
        if new_head in zeleni:
            zeleni.remove(new_head)
            snake.append(new_head)
        else:
            snake = snake[1:]
            snake.append(new_head)

    return tuple(snake), tuple(zeleni)


def levo(snake, zeleni):
    head = snake[-1]
    head_x = head[0]
    head_y = head[1]

    if head_x - 1 >= 0 and (head_x - 1, head_y) not in snake:
        new_head = (head_x - 1, head_y)
        if new_head in zeleni:
            zeleni.remove(new_head)
            snake.append(new_head)
        else:
            snake = snake[1:]
            snake.append(new_head)

    return tuple(snake), tuple(zeleni)



class Snake(Problem):


    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        #ja definirame goleminata na tablata
        self.grid_size = [10,10]


    def successor(self, state):
        successors = dict()

        #(snake,nasoka, zeleni)
        snake = list(state[0])
        nasoka = state[1]
        zeleni_jabolki = list(state[2])

        # ProdolzhiPravo
        if nasoka == "JUG":
            new_nasoka = nasoka
            new_snake, new_zeleni_jabolki = dolu(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["ProdolzhiPravo"] = (new_snake, new_nasoka, new_zeleni_jabolki)
        elif nasoka == "SEVER":
            new_nasoka = nasoka
            new_snake, new_zeleni_jabolki = gore(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["ProdolzhiPravo"] = (new_snake, new_nasoka, new_zeleni_jabolki)

        elif nasoka == "ISTOK":
            new_nasoka = nasoka
            new_snake, new_zeleni_jabolki = desno(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["ProdolzhiPravo"] = (new_snake, new_nasoka, new_zeleni_jabolki)

        elif nasoka == "ZAPAD":
            new_nasoka = nasoka
            new_snake, new_zeleni_jabolki = levo(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["ProdolzhiPravo"] = (new_snake, new_nasoka, new_zeleni_jabolki)
        # SvrtiDesno
        if nasoka == "JUG":
            new_nasoka = "ZAPAD"
            new_snake, new_zeleni_jabolki = levo(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["SvrtiDesno"] = (new_snake, new_nasoka, new_zeleni_jabolki)
        elif nasoka == "SEVER":
            new_nasoka = "ISTOK"
            new_snake, new_zeleni_jabolki = desno(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["SvrtiDesno"] = (new_snake, new_nasoka, new_zeleni_jabolki)
        elif nasoka == "ISTOK":
            new_nasoka = "JUG"
            new_snake, new_zeleni_jabolki = dolu(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["SvrtiDesno"] = (new_snake, new_nasoka, new_zeleni_jabolki)
        elif nasoka == "ZAPAD":
            new_nasoka = "SEVER"
            new_snake, new_zeleni_jabolki = gore(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["SvrtiDesno"] = (new_snake, new_nasoka, new_zeleni_jabolki)
        # SvrtiLevo
        if nasoka == "JUG":
            new_nasoka = "ISTOK"
            new_snake, new_zeleni_jabolki = desno(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["SvrtiLevo"] = (new_snake, new_nasoka, new_zeleni_jabolki)
        elif nasoka == "SEVER":
            new_nasoka = "ZAPAD"
            new_snake, new_zeleni_jabolki = levo(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["SvrtiLevo"] = (new_snake, new_nasoka, new_zeleni_jabolki)
        elif nasoka == "ISTOK":
            new_nasoka = "SEVER"
            new_snake, new_zeleni_jabolki = gore(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["SvrtiLevo"] = (new_snake, new_nasoka, new_zeleni_jabolki)
        elif nasoka == "ZAPAD":
            new_nasoka = "JUG"
            new_snake, new_zeleni_jabolki = dolu(snake, zeleni_jabolki)
            if new_snake != snake:
                successors["SvrtiLevo"] = (new_snake, new_nasoka, new_zeleni_jabolki)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0

    def h(self, node):
        distances = [abs(node.state[0][-1][0] - el[0]) + abs(node.state[0][-1][1] - el[1]) for el in node.state[2]]
        if len(distances) != 0:
            return sum(distances) / len(distances)
        return 0


if __name__ == '__main__':
    initial_state = ((0, 7),(0, 8),(0, 9))
    nasoka = "JUG"

    n = int(input())
    zeleni_jabolki = [tuple(map(int, input().split(','))) for _ in range(n)]


    problem_snake = Snake((initial_state,nasoka,tuple(zeleno for zeleno in zeleni_jabolki)))
    print(astar_search(problem_snake).solution())