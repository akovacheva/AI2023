from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search,recursive_best_first_search

class Football(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(state, opponents):
        man_pos = state[0]
        ball_pos = state[1]
        for opp in opponents:
            if man_pos == opp or ball_pos == opp:
                return False
        return man_pos[0] >= 0 and man_pos[0] < 8 and \
                man_pos[1] >= 0 and man_pos[1] < 6 and \
                ball_pos[0] >= 0 and ball_pos[0] < 8 and \
                ball_pos[1] >= 0 and ball_pos[1] < 6


    def successor(self, state):
        man_pos, ball_pos = state[0], state[1]
        successors = dict()

        for move in ["gore", "dolu", "desno", "gore-desno", "dolu-desno"]:
            new_man_pos = None
            new_ball_pos = None

            if move == "gore":
                new_man_pos = (man_pos[0] - 1, man_pos[1])
                if new_man_pos == ball_pos:
                    new_ball_pos = (new_man_pos[0] - 1, new_man_pos[1])
            elif move == "dolu":
                new_man_pos = (man_pos[0] + 1, man_pos[1])
                if new_man_pos == ball_pos:
                    new_ball_pos = (new_man_pos[0] + 1, new_man_pos[1])
            elif move == "desno":
                new_man_pos = (man_pos[0], man_pos[1] + 1)
                if new_man_pos == ball_pos:
                    new_ball_pos = (new_man_pos[0], new_man_pos[1] + 1)
            elif move == "gore-desno":
                new_man_pos = (man_pos[0] - 1, man_pos[1] + 1)
                if new_man_pos == ball_pos:
                    new_ball_pos = (new_man_pos[0] - 1, new_man_pos[1] + 1)
            elif move == "dolu-desno":
                new_man_pos = (man_pos[0] + 1, man_pos[1] + 1)
                if new_man_pos == ball_pos:
                    new_ball_pos = (new_man_pos[0] + 1, new_man_pos[1] + 1)

            if new_man_pos and self.check_valid(new_man_pos, ball_pos):
                if new_ball_pos and self.check_valid(new_ball_pos, None):
                    successors["Turni topka " + move] = ((new_man_pos, new_ball_pos),)
                else:
                    successors["Pomesti coveche " + move] = ((new_man_pos, ball_pos),)

        return successors

    def h(self, node):
        man_pos, ball_pos = node.state[0], node.state[1]
        goal1, goal2 = self.goal
        return min(abs(man_pos[0] - goal1[0]) + abs(man_pos[1] - goal1[1]),
                   abs(man_pos[0] - goal2[0]) + abs(man_pos[1] - goal2[1])) + \
               abs(ball_pos[0] - goal1[0]) + abs(ball_pos[1] - goal1[1]) + \
               abs(ball_pos[0] - goal2[0]) + abs(ball_pos[1] - goal2[1])


if __name__ == '__main__':
    man_pos = tuple(map(int, input().split(',')))
    ball_pos = tuple(map(int, input().split(',')))
    initial_state = (man_pos, ball_pos)
    goal_state = ((7, 2), (7, 3))
    opponents = [(3, 3), (5, 4)]
    football = Football(initial_state, goal_state)

    result = astar_search(football)
    solution = result.solution()
    print(solution)









