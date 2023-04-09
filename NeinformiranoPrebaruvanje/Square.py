from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def pomestiGore(x,y):
    return x, y + 1

def pomestiDolu(x,y):
    return x, y - 1

def pomestiLevo(x,y):
    return x - 1, y

def pomestiDesno(x,y):
    return x + 1, y

class Squares(Problem):
    def __init__(self, initial, house):
        super().__init__(initial, house)
        self.grid_size = [5,5]



    @staticmethod
    def check_valid(state):
        for x, y in state:
            if x[0] < 0 or x[0] > 4 or y[1] < 0 or y[1] > 4:
                return False
        return True

    # „Pomesti kvadratche X levo / desno / gore / dolu“
    def successor(self, state):
        succ = dict()
        # ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))

        x1,y1 = state[0]
        x2,y2 = state[1]
        x3,y3 = state[2]
        x4,y4 = state[3]
        x5,y5 = state[4]


        #PrvKvadrat

        if self.check_valid((x1,y1)):
            #levo
            if x1 > 0:
                succ['Pomesti kvadratche 1 levo'] = ((pomestiLevo(x1, y1)), (x2, y2), (x3, y3), (x4, y4), (x5, y5))
            #desno
            if x1 < self.grid_size[0]:
                succ['Pomesti kvadratche 1 desno'] = ((pomestiDesno(x1, y1)), (x2, y2), (x3, y3), (x4, y4), (x5, y5))
            #gore
            if y1 < self.grid_size[1]:
                succ['Pomesti kvadratche 1 gore'] = ((pomestiGore(x1, y1)),(x2, y2), (x3, y3), (x4, y4), (x5, y5))
            #dolu
            if y1 > 0:
                succ['Pomesti kvadratche 1 dolu'] = ((pomestiDolu(x1, y1)), (x2, y2), (x3, y3), (x4, y4), (x5, y5))


        #VtorKvadrat
        elif self.check_valid((x2, y2)):
            #levo
            if x2 > 0:
                succ['Pomesti kvadratche 2 levo'] = ((x1, y1), (pomestiLevo(x2, y2)), (x3, y3), (x4, y4), (x5, y5))
            #desno
            if x2 < self.grid_size[0]:
                succ['Pomesti kvadratche 2 desno'] = ((x1, y1), (pomestiDesno(x2, y2)), (x3, y3), (x4, y4), (x5, y5))
            #gore
            if y2 < self.grid_size[1]:
                succ['Pomesti kvadratche 2 gore'] = ((x1, y1), (pomestiGore(x2, y2)), (x3, y3), (x4, y4), (x5, y5))
            #dolu
            if y2 > 0:
                succ['Pomesti kvadratche 2 dolu'] = ((x1, y1), (pomestiDolu(x2, y2)), (x3, y3), (x4, y4), (x5, y5))


        #TretKvadrat
        elif self.check_valid(x3, y3):
            #levo
            if x3 > 0:
                succ['Pomesti kvadratche 3 levo'] = ((x1, y1), (x2, y2), (pomestiLevo(x3, y3)), (x4, y4), (x5, y5))
            #desno
            if x3 < self.grid_size[0]:
                succ['Pomesti kvadratche 3 desno'] = ((x1, y1), (x2, y2), (pomestiDesno(x3, y3)), (x4, y4), (x5, y5))
            #gore
            if y3 < self.grid_size[1]:
                succ['Pomesti kvadratche 3 gore'] = ((x1, y1), (x2, y2), (pomestiGore(x3, y3)), (x4, y4), (x5, y5))
            #dolu
            if y3 > 0:
                succ['Pomesti kvadratche 3 dolu'] = ((x1, y1), (x2, y2), (pomestiDolu(x3, y3)), (x4, y4), (x5, y5))


        #CetvrtKvadrat
        elif self.check_valid(x4, y4):
            #levo
            if x4 > 0:
                succ['Pomesti kvadratche 1 levo'] = ((x1, y1), (x2, y2), (x3, y3), (pomestiLevo(x4, y4)), (x5, y5))
            #desno
            if x4 < self.grid_size[0]:
                succ['Pomesti kvadratche 1 desno'] = ((x1, y1), (x2, y2), (x3, y3), (pomestiDesno(x4, y4)), (x5, y5))
            #gore
            if y4 < self.grid_size[1]:
                succ['Pomesti kvadratche 1 gore'] = ((x1, y1), (x2, y2), (x3, y3), (pomestiGore(x4, y4)), (x5, y5))
            #dolu
            if y4 > 0:
                succ['Pomesti kvadratche 1 dolu'] = ((x1, y1), (x2, y2), (x3, y3), (pomestiDolu(x4, y4)), (x5, y5))

        #PettiKvadrat
        elif self.check_valid((x5, y5)):
            #levo
            if x5 > 0:
                succ['Pomesti kvadratche 1 levo'] = ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (pomestiLevo(x5, y5)))
            #desno
            if x5 < self.grid_size[0]:
                succ['Pomesti kvadratche 1 desno'] = ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (pomestiDesno(x5, y5)))
            #gore
            if y5 < self.grid_size[1]:
                succ['Pomesti kvadratche 1 gore'] = ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (pomestiGore(x5, y5)))
            #dolu
            if y5 > 0:
                succ['Pomesti kvadratche 1 dolu'] = ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (pomestiDolu(x5, y5)))



            return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

if __name__ == '__main__':
    # ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))
    # initial_state = tuple()
    # for _ in range(5):
    #     initial_state += (tuple(map(int, input().split(','))), )

    initial_state = ((2, 4), (1, 3), (2, 2), (3, 1), (4, 0))
    goal_state = ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0))

    squares = Squares(initial_state, goal_state)

    print(breadth_first_graph_search(squares).solution())