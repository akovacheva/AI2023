from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search


class Puzzle(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        """
        state = '*32415678'
                0 1 2
                3 4 5
                6 7 8
        """
        succ = {}

        # go barame indexot na praznoto pole
        ind = state.index("*")


        #dvizenje na prazno pole

        #up i - 3, i -> im menuvame indexi, ne moze ako e vo prviot red
        if ind >= 3:
        #go pretvorame indexot vo lista
            tmp = list(state)
            tmp[ind], tmp[ind-3] = tmp[ind-3], tmp[ind]
            new_state = ''.join(tmp) #gi spojuvame elementite od listata za da gi vratime vo string
            succ["Up"] = new_state

        #down
        if ind <= 5:
            tmp = list(state)
            tmp[ind], tmp[ind + 3] = tmp[ind + 3], tmp[ind]
            new_state = ''.join(tmp)
            succ["Down"] = new_state

        #left
        if ind % 3 != 0:
            tmp = list(state)
            tmp[ind], tmp[ind - 1] = tmp[ind - 1], tmp[ind]
            new_state = ''.join(tmp)
            succ["Left"] = new_state

        #right
        if ind != 2 and ind != 5 and ind != 8:
            tmp = list(state)
            tmp[ind], tmp[ind + 1] = tmp[ind + 1], tmp[ind]
            new_state = ''.join(tmp)
            succ["Right"] = new_state

        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        # broj na polinja koi ne se na vistinskoto mesto
        counter = 0 # brojac za kolku polinja ne se na vistinskoto mesto

        """ 
        a = [1, 2, 3] b = ['a', 'b', 'c']
        zip(a, b) = [(1, 'a'), (2, 'b'), (3, 'c')]
        """

        for x,y in zip(node.state, self.goal):
            # momentalna, celna sostojba
            if x != y:
                counter += 1

        return counter




if __name__ == '__main__':
    puzzle = Puzzle('*32415678', '*12345678')
    result1 = greedy_best_first_graph_search(puzzle)
    print(result1.solve())
    result2 = astar_search(puzzle)
    print(result2.solve())
    result3 = recursive_best_first_search(puzzle)
    print(result3.solve())