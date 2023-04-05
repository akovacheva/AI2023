# Пример - Два сада
# Дадени се два сада J0 и J1, со капацитети C0 и C1 литри, соодветно.
# Да се доведат до состојба во која J0 има G0 литри, а J1 има G1 литри. Акции:
#
# Испразни кој било од садовите
# Претури течност од еден во друг сад, со тоа што не може да се надмине капацитетот на садот
# Наполни кој било од садовите (за дома)
# Дефиниција на состојба
# Торка (X, Y) која означува дека J0 содржи X литри, а J1 содржи Y литри.
# Опционална вредност '*', која означува дека е небитно колку литри има во садот.
# Цел: Предефинираната состојба до која сакаме да стигнеме.
# Ако нѐ интересира само едниот сад, за другиот можеме да ставиме '*'.


from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Container(Problem):

    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)
        self.capacities = capacities


    #so koi akcii preminuvame vo sledni sostojbi
    def successor(self, state):
        #(j0,j1)

        successors = dict()
        j0, j1 = state #dadeni od sostojbata
        c0,c1 = self.capacities

        #AKCIJA NA PRAZNENJE NA SAD

        #vo koj slucaj ne moze da ispraznime sad
        #ako e vekje prazen

        if j0 > 0:
            successors["Isprazni go sadot j0"] = (0,j1)
        if j1 > 0:
            successors["Isprazni go sadot j1"] = (j0, 0)

        #PRETURANJE OD J1 VO J0 I OBRATNO

        #Od jo vo j1:

        if j0 > 0 and j1 < c1:
            delta = min(c1 - j1,j0) #ja zemame pomalata vrednost
            successors["Preturi od j0 vo j1"] = (j0-delta,j1+delta)
        if j1 > 0 and j0 < c0:
            delta = min(c0 - j0,j1)
            successors["Preturi od j1 vo j0"] = (j0+delta,j1-delta)

        return successors




    #site mozni akcii nad sostojbata state
    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]
    #gledame koja sostojba ke se dobie za odredena akcija

    #celna sostojba
    def goal_test(self, state):
        return state == self.goal
    #dali momentalnata sostojba e ednakva so celnata


if __name__ == '__main__':
# ja instancirame klasata
    container = Container([15,5],(5,5),(10,0))

    result = breadth_first_graph_search(container)
    print(result.solution())
    print(result.solve())

    result1 = depth_first_graph_search(container)
    print(result1.solution())
    print(result1.solve())