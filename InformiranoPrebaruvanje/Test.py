from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search
from searching_framework.informed_search import astar_search


class Snake(Problem):
    def __init__(self, initial, goal, board_size):
        super().__init__(initial, goal)
        self.board_size = board_size

    def successor(self, state):
        succ = {}

        # Define current head position and body
        head_pos = state[0]
        body = state[1:]

        # Define possible new head positions
        possible_head_positions = [(head_pos[0] + 1, head_pos[1]),  # move right
                                   (head_pos[0] - 1, head_pos[1]),  # move left
                                   (head_pos[0], head_pos[1] + 1),  # move up
                                   (head_pos[0], head_pos[1] - 1)]  # move down

        # Filter out positions that are outside the board or on the body
        possible_head_positions = [pos for pos in possible_head_positions if
                                   pos[0] >= 0 and pos[0] < self.board_size and
                                   pos[1] >= 0 and pos[1] < self.board_size and
                                   pos not in body]

        # Define the next state for each possible new head position
        for pos in possible_head_positions:
            new_body = list(body)
            if pos in self.goal:
                new_body.append(pos)
            else:
                new_body = new_body[1:] + [pos]
            new_body = tuple(new_body)

            succ[("h", pos, tuple(new_body))] = (pos,) + tuple(new_body)

        return succ


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state = node.state
        head_pos = state[0]
        body = state[1:]

        # Define the distance to the closest green apple
        distances = [abs(head_pos[0] - apple[0]) + abs(head_pos[1] - apple[1]) for apple in self.goal]
        min_distance = min(distances) if distances else 0

        # Define the distance to the closest body part
        if len(body) > 1:
            body_distances = [abs(head_pos[0] - part[0]) + abs(head_pos[1] - part[1]) for part in body[:-1]]
            min_body_distance = min(body_distances) if body_distances else 0
        else:
            min_body_distance = 0

        # Return the sum of the distances
        return min_distance + min_body_distance


if __name__ == "__main__":
    n = int(input())
    zeleni_jabolki = [tuple(map(int, input().split(','))) for _ in range(n)]

    board_size = 10
    initial_state = ((3, 0), (2, 0), (1, 0))
    goal_state = initial_state + tuple(zeleni_jabolki)

    problem = Snake(initial_state, zeleni_jabolki, board_size)
    solution = astar_search(problem)

    # Print the sequence of movements
    for action in solution.path():
        print(action[0])
