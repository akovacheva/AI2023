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
        head_x = state[3]
        head_y = state[4]

        body = zmija[1]
        tail = zmija[-1]

        print(head_x)
        #ProdolzhiPravo

        if nasoka == "SEVER":
            if head_y + 1 < self.grid_size[1] and (head_x, head_y + 1) not in self.lista_crveni and (head_x, head_y + 1) not in body:
                if (head_x, head_y + 1) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['ProdolzhiPravo'] = ((head_x,head_y + 1), tuple(zeleni_jabolki), "SEVER")
                else:
                    successors['ProdolzhiPravo'] = ((head_x, head_y + 1), tuple(zeleni_jabolki), "SEVER")

        if nasoka == "JUG":
            if head_y - 1 > 0 and (head_x, head_y - 1) not in self.lista_crveni and (head_x, head_y - 1) not in body:
                if (head_x, head_y - 1) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['ProdolzhiPravo'] = ((head_x,head_y - 1), tuple(zeleni_jabolki), "JUG")
                else:
                    successors['ProdolzhiPravo'] = ((head_x, head_y - 1), tuple(zeleni_jabolki), "JUG")

        if nasoka == "ZAPAD":
            if head_x - 1 > 0 and (head_x - 1, head_y) not in self.lista_crveni and (head_x - 1, head_y) not in body:
                if (head_x - 1, head_y) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['ProdolzhiPravo'] = ((head_x - 1,head_y), tuple(zeleni_jabolki), "ZAPAD")
                else:
                    successors['ProdolzhiPravo'] = ((head_x - 1, head_y), tuple(zeleni_jabolki), "ZAPAD")

        if nasoka == "ISTOK":
            if head_x + 1 < self.grid_size[0] and (head_x + 1, head_y) not in self.lista_crveni and (head_x + 1, head_y) not in body:
                if (head_x + 1, head_y) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['ProdolzhiPravo'] = ((head_x + 1,head_y), tuple(zeleni_jabolki), "ISTOK")
                else:
                    successors['ProdolzhiPravo'] = ((head_x + 1, head_y), tuple(zeleni_jabolki), "ISTOK")


        #SvrtiDesno

        if nasoka == "SEVER":
            if head_x + 1 < self.grid_size[0] and (head_x + 1, head_y) not in self.lista_crveni and (head_x + 1, head_y) not in body:
                if (head_x + 1, head_y) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['SvrtiDesno'] = ((head_x + 1,head_y), tuple(zeleni_jabolki), "ISTOK")
                else:
                    successors['SvrtiDesno'] = ((head_x + 1, head_y), tuple(zeleni_jabolki), "ISTOK")

        if nasoka == "JUG":
            if head_x - 1 > 0 and (head_x - 1, head_y) not in self.lista_crveni and (head_x - 1, head_y) not in body:
                if (head_x - 1, head_y) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x, head_y))
                    successors['SvrtiDesno'] = ((head_x - 1,head_y), tuple(zeleni_jabolki), "ZAPAD")
                else:
                    successors['SvrtiDesno'] = ((head_x - 1, head_y), tuple(zeleni_jabolki), "ZAPAD")


        if nasoka == "ZAPAD":
            if head_y + 1 < self.grid_size[1] and (head_x, head_y + 1) not in self.lista_crveni and (head_x, head_y + 1) not in body:
                if (head_x, head_y + 1) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['SvrtiDesno'] = ((head_x, head_y + 1), tuple(zeleni_jabolki), "SEVER")
                else:
                    successors['SvrtiDesno'] = ((head_x, head_y + 1), tuple(zeleni_jabolki), "SEVER")

        if nasoka == "ISTOK":
            if head_y - 1 > 0 and (head_x, head_y - 1) not in self.lista_crveni and (head_x, head_y - 1) not in body:
                if (head_x, head_y - 1) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x, head_y))
                    successors['SvrtiDesno'] = ((head_x, head_y - 1), tuple(zeleni_jabolki), "JUG")
                else:
                    successors['SvrtiDesno'] = ((head_x, head_y - 1), tuple(zeleni_jabolki), "JUG")

        #SvrtiLevo

        if nasoka == "SEVER":
            if head_x - 1 > 0 and (head_x - 1, head_y) not in self.lista_crveni and (head_x - 1, head_y) not in body:
                if (head_x - 1, head_y) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['SvrtiLevo'] = ((head_x - 1,head_y), tuple(zeleni_jabolki), "ZAPAD")
                else:
                    successors['SvrtiLevo'] = ((head_x - 1, head_y), tuple(zeleni_jabolki), "ZAPAD")

        if nasoka == "JUG":
            if head_x + 1 < self.grid_size[0] and (head_x + 1, head_y) not in self.lista_crveni and (head_x + 1, head_y) not in body:
                if (head_x + 1, head_y) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['SvrtiLevo'] = ((head_x + 1,head_y), tuple(zeleni_jabolki), "ISTOK")
                else:
                    successors['SvrtiLevo'] = ((head_x + 1, head_y), tuple(zeleni_jabolki), "ISTOK")

        if nasoka == "ZAPAD":
            if head_y - 1 > 0 and (head_x, head_y - 1) not in self.lista_crveni and (head_x, head_y - 1) not in body:
                if (head_x, head_y - 1) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['SvrtiLevo'] = ((head_x, head_y - 1), tuple(zeleni_jabolki), "JUG")
                else:
                    successors['SvrtiLevo'] = ((head_x, head_y - 1), tuple(zeleni_jabolki), "JUG")

        if nasoka == "ISTOK":
            if head_y + 1 < self.grid_size[1] and (head_x, head_y + 1) not in self.lista_crveni and (head_x, head_y + 1) not in body:
                if (head_x, head_y + 1) in zeleni_jabolki:
                    zmija = list(zmija)
                    zmija.append(tail)
                    zeleni_jabolki.remove((head_x,head_y))
                    successors['SvrtiLevo'] = ((head_x, head_y + 1), tuple(zeleni_jabolki), "SEVER")
                else:
                    successors['SvrtiLevo'] = ((head_x, head_y + 1), tuple(zeleni_jabolki), "SEVER")


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0


if __name__ == '__main__':

    # n = int(input())
    # lista_zeleni = []
    nasoka = "JUG"

    lista_zeleni = [(6, 9), (2, 7), (9, 5), (2, 3), (4, 3)]

    lista_crveni = [(4, 6), (6, 5), (3, 3), (6, 8)]

    # for i in range(n):
    #     z_j = input()
    #     z_j_koord = tuple(z_j.split(","))
    #     lista_zeleni.append(z_j_koord)
    #
    # m = int(input())
    # lista_crveni = []
    # for i in range(m):
    #     c_j = input()
    #     c_j_koord = tuple(c_j.split(","))
    #     lista_crveni.append(c_j_koord)

    zmija = ((0, 7), (0, 8), (0, 9))

    problem = Snake((zmija,tuple(lista_zeleni),nasoka), lista_crveni)




    print(breadth_first_graph_search(problem).solution())
