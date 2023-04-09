import math

from searching_framework.utils import Problem
from searching_framework.uninformed_search import *



class Topcinja(Problem):
    def __init__(self, initial, prepreki, n, goal=None):
        super().__init__(initial, goal)
        self.prepreki = prepreki
        self.grid_size = n

    def successor(self, state):
        succ = dict()
        #((x1,y1),(x2,y2)...(xn,yn))

        for tocka in state:
            x,y = tocka
            #Gore-Levo
            remove = (x - 1, y + 1)
            nova_poz = (x - 2, y + 2)
            # tocka(2,0) -> rem(1,1) -> new(0,2)
            if x - 2 >= 0 and y + 2 < self.grid_size and remove in state and nova_poz not in state:
                #so ova kreirame nova lista bez remove i bez
                # prethodnata pozicija na tockata koja ja pomestivme
                lista = [t for t in state if t != remove and t != tocka]
                lista.append(nova_poz)
                #so ova ja obelezuvame novata sostojba na listata
                #otkako ke se pomesti topceto i ke se izbrise nekoe, soodvetno
                succ[f'Gore Levo: (x={x},y={y}'] = tuple(lista)

            # GoreDesno
            remove = (x + 1, y + 1)
            nova_poz = (x + 2, y + 2)

            if x + 2 < self.grid_size and y + 2 < self.grid_size and remove in state and nova_poz not in state:
                lista = [t for t in state if t != remove and t != tocka]
                lista.append(nova_poz) #ja dodavame novata pozicija vo listata
                succ[f'Gore Desno: (x={x},y={y}'] = tuple(lista)

            #DoluLevo
            remove = (x - 1, y - 1)
            nova_poz = (x - 2, y - 2)

            if x - 2 >= 0 and y - 2 >= 0 and remove in state and nova_poz not in state:
                lista = [t for t in state if t != remove and t != tocka]
                lista.append(nova_poz)
                succ[f'Dolu Levo: (x={x},y={y}'] = tuple(lista)

            #DoluDesno
            remove = (x + 1, y - 1)
            nova_poz = (x + 2, y - 2)
            if x + 2 < self.grid_size and y - 2 >= 0 and remove in state and nova_poz not in state:
                lista = [t for t in state if t != remove and t != tocka]
                lista.append(nova_poz)
                succ[f'Dolu Desno: (x={x},y={y}'] = tuple(lista)

            #Levo
            remove = (x - 1, y)
            nova_poz = (x - 2, y)

            if x - 2 >= 0 and remove in state and nova_poz not in state:
                lista = [t for t in state if t != remove and t != tocka]
                lista.append(nova_poz)
                succ[f'Levo: (x={x},y={y}'] = tuple(lista)

            #Desno
            remove = (x + 1, y)
            nova_poz = (x + 2, y)

            if x + 2 < self.grid_size and remove in state and nova_poz not in state:
                lista = [t for t in state if t != remove and t != tocka]
                lista.append(nova_poz)
                succ[f'Desno: (x={x},y={y}'] = tuple(lista)

        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        end = (math.floor(self.grid_size/2), self.grid_size-1)
        return len(state)==1 and state[0] == end

if __name__ == '__main__':
    # #dimenzii
    # n = int(input())
    # #br.topcinja
    # m = int(input())
    # topcinja = []
    # for topce in range(m):
    #     topcinja.append(tuple(map(int, input().split(','))))
    #
    # p = int(input())
    # prepreki = []
    # for prepreka in range(p):
    #     prepreki.append(tuple(map(int, input().split(","))))

    n = 5
    m = 5
    topcinja = [(2, 0), (1, 1), (1, 2), (1, 3), (1, 4)]

    p = 4
    prepreki = [(4, 1), (4, 2), (4, 3), (4, 4)]


    # initial_state = tuple(topcinja)
    # prep = tuple(prepreki)
    #
    topki = Topcinja(tuple(topcinja),tuple(prepreki),n)

    print(breadth_first_graph_search(topki).solution())