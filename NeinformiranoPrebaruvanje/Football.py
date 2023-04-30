from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Football(Problem):
    def __init__(self, initial, gol, opponents ,goal=None):
        super().__init__(initial, goal)
        self.gol = gol
        self.opponents = opponents
        self.grid_size = [8, 6]

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == gol[0] or state == gol[1]


# Ni proveruva da ne izleze od tablata ii da ne se naogjaat na ista pozicija
    @staticmethod
    def check_valid(state, opponents):
        man_pos = state[0]
        ball_pos = state[1]

        if man_pos == opponents or ball_pos == opponents:
            return False

        return man_pos[0] >= 0 and man_pos[0] < 8 and \
                man_pos[1] >= 0 and man_pos[1] < 6 and \
                ball_pos[0] >= 0 and ball_pos[0] < 8 and \
                ball_pos[1] >= 0 and ball_pos[1] < 6

    def successor(self, state):
        successors = dict()
        new_man = None
        #definiranje sostojba -> (covece, topka)

        #Gore
        if self.check_valid((self.man_pos[0], self.man_pos[1] + 1), self.opponents) and ball_pos not in forbbiden:
            if (man_pos[0], man_pos[1] + 1) in [(ball_pos[0] - 1, ball_pos[1] - 1), (ball_pos[0] - 1, ball_pos[1]), (ball_pos[0] - 1, ball_pos[1] + 1),
                                                (ball_pos[0], ball_pos[1] - 1), (ball_pos[0], ball_pos[1] + 1), (ball_pos[0] + 1, ball_pos[1] - 1),
                                                (ball_pos[0] + 1, ball_pos[1]), (ball_pos[0] + 1, ball_pos[1] + 1)]:

                if (self.man_pos[0] + 1, self.man_pos[1]) == (ball_pos[0], ball_pos[1]):

                    new_man = (ball_pos[0],ball_pos[1])

                    successors['Turni topka desno'] = (ball_pos[0] + 1, ball_pos[1]), new_man

                elif (man_pos[0] + 1, man_pos[1] - 1) == (ball_pos[0], ball_pos[1]):

                    new_man = ball_pos
                    successors['Turni topka dolu-desno'] = (ball_pos[0] + 1, ball_pos[1]), new_man

            successors['Pomesti coveche gore'] = (man_pos[0], man_pos[1] + 1)


        #     #Dolu
        # if self.check_valid((man_pos[0], man_pos[1] - 1), self.opponents) and ball_pos not in forbbiden:
        #     if (man_pos[0], man_pos[1] - 1) in [(ball_pos[0] - 1, ball_pos[1] - 1), (ball_pos[0] - 1, ball_pos[1]), (ball_pos[0] - 1, ball_pos[1] + 1),
        #                                         (ball_pos[0], ball_pos[1] - 1), (ball_pos[0], ball_pos[1] + 1), (ball_pos[0] + 1, ball_pos[1] - 1),
        #                                         (ball_pos[0] + 1, ball_pos[1]), (ball_pos[0] + 1, ball_pos[1] + 1)]:
        #
        #         if (man_pos[0] + 1, man_pos[1]) == (ball_pos[0], ball_pos[1]):
        #             new_man = ball_pos
        #             successors['Turni topka desno'] = (ball_pos[0] + 1, ball_pos[1])
        #
        #         elif (man_pos[0] + 1, man_pos[1] - 1) == (ball_pos[0], ball_pos[1]):
        #
        #             new_man = ball_pos
        #             successors['Turni topka dolu-desno'] = (ball_pos[0] + 1, ball_pos[1])
        #
        #         elif (man_pos[0] + 1, man_pos[1] + 1) == (ball_pos[0], ball_pos[1]):
        #
        #             new_man = ball_pos
        #             successors['Turni topka dolu-desno'] = (ball_pos[0] + 1, ball_pos[1])
        #
        #     successors['Pomesti coveche dolu'] = (man_pos[0], man_pos[1] - 1)


        return successors


if __name__ == '__main__':
    man_pos = tuple(map(int, input().split(',')))
    ball_pos = tuple(map(int, input().split(',')))

    opponents = [(3, 3), (5, 4)]
    gol = [(7, 2), (7, 3)]
    forbbiden = [(2, 2),(2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4), (4, 5), (5, 3), (5, 5), (6, 3), (6, 4), (6, 5)]

    problem = Football((man_pos, ball_pos), gol, opponents)
    print(breadth_first_graph_search(problem).solution())

