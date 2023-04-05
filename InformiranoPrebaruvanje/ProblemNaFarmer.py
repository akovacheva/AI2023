from searching_framework.utils import Problem
from searching_framework.informed_search import astar_search

def valid(state):
    farmer, volk, jare, zelka = state

    if volk == jare and farmer != volk:
        return False
    if jare == zelka and farmer != jare:
        return False
    return True


class Farmer(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
    #(farmer, volj, jare,zelka)

        successors = dict()
        # sostojba
        farmer, volk, jare, zelka = state

        #Definirame akcii

        #Farmer se prenesuvas ebesi
        farmer_new = 'e' if farmer == 'w' else 'w'
        state_new = farmer_new,volk,jare,zelka
        if valid(state_new):
            successors['Framer_nosi_farmer'] = state_new

        #Farmer prenesuva volk

        if farmer == volk:
            volk_new = 'e' if farmer == 'w' else 'w'
            state_new = farmer_new,volk_new,jare,zelka
            if valid(state_new):
                successors['Framer_nosi_volk'] = state_new

        #Farmer prenesuva jare

        if farmer == jare:
            jare_new = 'e' if farmer == 'w' else 'w'
            state_new = farmer_new,volk,jare_new,zelka
            if valid(state_new):
                successors['Framer_nosi_jare'] = state_new

        #Farmer prenesuva zelka

        if farmer == zelka:
            zelka_new = 'e' if farmer == 'w' else 'w'
            state_new = farmer_new,volk,jare,zelka_new
            if valid(state_new):
                successors['Framer_nosi_zelka'] = state_new

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):

        state = node.state
        goal = self.goal

        value = 0

        for x,y in zip(state,goal):
            if x != y:
                value += 1

        return value


if __name__ == '__main__':
    initial_state = ("e","e","e","e")
    goal_state = ("w","w","w","w")

    farmer = Farmer(initial_state,goal_state)
    answer = astar_search(farmer)
    print(answer.solution())