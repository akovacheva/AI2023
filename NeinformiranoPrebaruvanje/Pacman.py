from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Pacman(Problem):
    def __init__(self, initial,obstacles_list, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [10, 10]
        self.obstacles_list = obstacles_list

    def successor(self, state):
        successors = dict()
        #state (pacman_x,pacman_y,nasoka,tocki)

        pacman_x = state[0]
        pacman_y = state[1]
        nasoka = state[2]
        tocki = state[3]

    #ProdolzhiPravo
        if nasoka == "istok":
            if pacman_x + 1 < self.grid_size[1] and (pacman_x + 1, pacman_y) not in self.obstacles_list:
                if (pacman_x + 1, pacman_y) in tocki:
                    tocki_lista = tuple(tocka for tocka in tocki if tocka != (pacman_x + 1, pacman_y)) #jade
                    successors["ProdolzhiPravo"] = (pacman_x + 1, pacman_y, nasoka, tuple(tocki_lista))
                else:
                    successors["ProdolzhiPravo"] = (pacman_x + 1, pacman_y, nasoka, tuple(tocki))

        if nasoka == "zapad":
            if pacman_x - 1 >= 0 and (pacman_x - 1, pacman_y) not in self.obstacles_list:
                if (pacman_x - 1, pacman_y) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x - 1, pacman_y)]  # jade
                    successors["ProdolzhiPravo"] = (pacman_x - 1, pacman_y, nasoka, tuple(tocki_lista))
                else:
                    successors["ProdolzhiPravo"] = (pacman_x - 1, pacman_y, nasoka, tuple(tocki))

        if nasoka == "sever":
            if pacman_y + 1 < self.grid_size[0] and (pacman_x, pacman_y + 1) not in self.obstacles_list:
                if (pacman_x, pacman_y + 1) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x, pacman_y + 1)]  # jade
                    successors["ProdolzhiPravo"] = (pacman_x, pacman_y + 1, nasoka, tuple(tocki_lista))
                else:
                    successors["ProdolzhiPravo"] = (pacman_x, pacman_y + 1, nasoka, tuple(tocki))

        if nasoka == "jug":
            if pacman_y - 1 >= 0 and (pacman_x, pacman_y - 1) not in self.obstacles_list:
                if (pacman_x, pacman_y - 1) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x, pacman_y - 1)]  # jade
                    successors["ProdolzhiPravo"] = (pacman_x, pacman_y - 1, nasoka, tuple(tocki_lista))
                else:
                    successors["ProdolzhiPravo"] = (pacman_x, pacman_y - 1, nasoka, tuple(tocki))

    #ProdolzhiNazad
        if nasoka == "istok":
            if pacman_x - 1 >= 0 and (pacman_x - 1, pacman_y) not in self.obstacles_list:
                if (pacman_x - 1, pacman_y) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x - 1, pacman_y) ] #jade
                    successors["ProdolzhiNazad"] = (pacman_x - 1, pacman_y, "zapad", tuple(tocki_lista))
                else:
                    successors["ProdolzhiNazad"] = (pacman_x - 1, pacman_y, "zapad", tuple(tocki))

        if nasoka == "zapad":
            if pacman_x + 1 < self.grid_size[0] and (pacman_x + 1, pacman_y) not in self.obstacles_list:
                if (pacman_x + 1, pacman_y) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x + 1, pacman_y)]  # jade
                    successors["ProdolzhiNazad"] = (pacman_x + 1, pacman_y, "istok", tuple(tocki_lista))
                else:
                    successors["ProdolzhiNazad"] = (pacman_x + 1, pacman_y, "istok", tuple(tocki))

        if nasoka == "sever":
            if pacman_y - 1 >= 0 and (pacman_x, pacman_y - 1) not in self.obstacles_list:
                if (pacman_x, pacman_y - 1) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x, pacman_y - 1)]  # jade
                    successors["ProdolzhiNazad"] = (pacman_x, pacman_y - 1, "jug", tuple(tocki_lista))
                else:
                    successors["ProdolzhiNazad"] = (pacman_x, pacman_y - 1, "jug", tuple(tocki))

        if nasoka == "jug":
            if pacman_y + 1 < self.grid_size[1] and (pacman_x, pacman_y + 1) not in self.obstacles_list:
                if (pacman_x, pacman_y + 1) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x, pacman_y + 1)]  # jade
                    successors["ProdolzhiNazad"] = (pacman_x, pacman_y + 1, "sever", tuple(tocki_lista))
                else:
                    successors["ProdolzhiNazad"] = (pacman_x, pacman_y + 1, "sever", tuple(tocki))

    #SvrtiLevo
        if nasoka == "istok":
            if pacman_y + 1 < self.grid_size[1] and (pacman_x, pacman_y + 1) not in self.obstacles_list:
                if (pacman_x, pacman_y + 1) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x, pacman_y + 1)] #jade
                    successors["SvrtiLevo"] = (pacman_x, pacman_y + 1, "sever", tuple(tocki_lista))
                else:
                    successors["SvrtiLevo"] = (pacman_x, pacman_y + 1, "sever", tuple(tocki))

        if nasoka == "zapad":
            if pacman_y - 1 >= 0 and (pacman_x, pacman_y - 1) not in self.obstacles_list:
                if (pacman_x, pacman_y - 1) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x, pacman_y - 1)]  # jade
                    successors["SvrtiLevo"] = (pacman_x, pacman_y - 1, "jug", tuple(tocki_lista))
                else:
                    successors["SvrtiLevo"] = (pacman_x, pacman_y - 1, "jug", tuple(tocki))

        if nasoka == "sever":
            if pacman_x - 1 >= 0 and (pacman_x - 1, pacman_y) not in self.obstacles_list:
                if (pacman_x - 1, pacman_y) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x - 1, pacman_y)]  # jade
                    successors["SvrtiLevo"] = (pacman_x - 1, pacman_y, "zapad", tuple(tocki_lista))
                else:
                    successors["SvrtiLevo"] = (pacman_x - 1, pacman_y, "zapad", tuple(tocki))

        if nasoka == "jug":
            if pacman_x + 1 < self.grid_size[1] and (pacman_x + 1, pacman_y) not in self.obstacles_list:
                if (pacman_x + 1, pacman_y) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x + 1, pacman_y)]  # jade
                    successors["SvrtiLevo"] = (pacman_x + 1, pacman_y, "istok", tuple(tocki_lista))
                else:
                    successors["SvrtiLevo"] = (pacman_x + 1, pacman_y, "istok", tuple(tocki))
    #SvrtiDesno
        if nasoka == "istok":
            if pacman_y - 1 >= 0 and (pacman_x, pacman_y - 1) not in self.obstacles_list:
                if (pacman_x, pacman_y - 1) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x, pacman_y - 1)] #jade
                    successors["SvrtiDesno"] = (pacman_x, pacman_y - 1, "jug", tuple(tocki_lista))
                else:
                    successors["SvrtiDesno"] = (pacman_x, pacman_y - 1, "jug", tuple(tocki))

        if nasoka == "zapad":
            if pacman_y + 1 < self.grid_size[1] and (pacman_x, pacman_y + 1) not in self.obstacles_list:
                if (pacman_x, pacman_y + 1) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x, pacman_y + 1)]  # jade
                    successors["SvrtiDesno"] = (pacman_x, pacman_y + 1, "sever", tuple(tocki_lista))
                else:
                    successors["SvrtiDesno"] = (pacman_x, pacman_y + 1, "sever", tuple(tocki))

        if nasoka == "sever":
            if pacman_x + 1 < self.grid_size[0] and (pacman_x + 1, pacman_y) not in self.obstacles_list:
                if (pacman_x + 1, pacman_y) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x + 1, pacman_y)]  # jade
                    successors["SvrtiDesno"] = (pacman_x + 1, pacman_y, "istok", tuple(tocki_lista))
                else:
                    successors["SvrtiDesno"] = (pacman_x + 1, pacman_y, "istok", tuple(tocki))

        if nasoka == "jug":
            if pacman_x - 1 >= 0 and (pacman_x - 1, pacman_y) not in self.obstacles_list:
                if (pacman_x - 1, pacman_y) in tocki:
                    tocki_lista = [tocka for tocka in tocki if tocka != (pacman_x - 1, pacman_y)]  # jade
                    successors["SvrtiDesno"] = (pacman_x - 1, pacman_y, "zapad", tuple(tocki_lista))
                else:
                    successors["SvrtiDesno"] = (pacman_x - 1, pacman_y, "zapad", tuple(tocki))


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


    def goal_test(self, state):

        return len(state[3]) == 0





if __name__ == "__main__":

    # obstacles_list=[[0,6], [0,8], [0,9], [1,2], [1,3], [1,4], [1,9],
    #                 [2,9], [3,6], [3,9],[4,1], [4,5], [4,6], [4,7], [5,1],
    #                 [5,6], [6,0], [6,1], [6,2], [6,9], [8,1], [8,4], [8,7], [8,8], [9,4], [9,7], [9,8]]

    obstacles_list=[(0,6), (0,8), (0,9), (1,2), (1,3), (1,4), (1,9),
                    (2,9), (3,6), (3,9),(4,1), (4,5), (4,6), (4,7), (5,1),
                    (5,6), (6,0), (6,1), (6,2), (6,9), (8,1), (8,4), (8,7), (8,8), (9,4), (9,7), (9,8)]

    x = int(input())
    y = int(input())

    nasoka = input()

    n = int(input())
    tocki = []

    for i in range(n):
        tocka = input()
        x_t, y_t = map(int, tocka.split(","))
        tocki.append((x_t, y_t))

    problem = Pacman((x, y, nasoka, tuple(tocki)), obstacles_list)
    print(breadth_first_graph_search(problem).solution())
