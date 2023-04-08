from searching_framework.utils import Problem
from searching_framework.uninformed_search import *




class Snake(Problem):

    def __init__(self, initial,lista_crveni, goal=None):
        super().__init__(initial, goal)
        self.grid_size  = [10,10]
        self.lista_crveni = lista_crveni

    def successor(self, state):
    # ([head,body,end],[z_j], nasoka) --> torka od listi
        successors = dict()
        zmija = state[0]
        zeleni_jabolki = state[1]
        nasoka = state[2]

        head = zmija[0]
        head_x = head[0]
        head_y = head[1]
        body = zmija[1]
        tail = zmija[-1]

        #ProdolzhiPravo

        if nasoka == "SEVER":
            if head_y + 1 < self.grid_size[1] and head not in lista_crveni and head not in body:
                if head in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['ProdolzhiPravo'] = ((head_x,head_y + 1), zeleni_jabolki, "SEVER")
                else:
                    successors['ProdolzhiPravo'] = ((head_x, head_y + 1), zeleni_jabolki, "SEVER")

        if nasoka == "JUG":
            if head_y - 1 > 0 and head not in lista_crveni and head not in body:
                if head in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['ProdolzhiPravo'] = ((head_x,head_y - 1), zeleni_jabolki, "JUG")
                else:
                    successors['ProdolzhiPravo'] = ((head_x, head_y - 1), zeleni_jabolki, "JUG")



        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1])


if __name__ == '__main__':

    n = int(input())
    lista_zeleni = []
    nasoka = "JUG"

    for i in range(n):
        z_j = input()
        z_j_koord = tuple(z_j.split(","))
        lista_zeleni.append(z_j_koord)

    m = int(input())
    lista_crveni = []
    for i in range(m):
        c_j = input()
        c_j_koord = tuple(c_j.split(","))
        lista_crveni.append(c_j_koord)

    zmija = ((0, 7), (0, 8), (0, 9))

    problem = Snake((zmija,lista_zeleni,nasoka),lista_crveni)
    print(breadth_first_graph_search(problem).solution())