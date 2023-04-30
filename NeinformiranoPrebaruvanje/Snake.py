from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Snake(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        #ja definirame goleminata na tablata
        self.grid_size = [10,10]


    def successor(self, state):
        successors = dict()
        # (x,y, (x_p1,y_p1,n_p1), (x_p2,y_p2,n_p2))
    #( (h_x,h_y),(b_x,b_y),(b_x1,b_y1)),
        # ((zj_x,zj_y) * n ),
        # ((cj_x,cj_y) * n )


        snake = list(state[0])
        head = snake[0]
        head_x = head[0]
        head_y = head[1]
        body = list(snake[1:])
        end = body[-1] if body else head  #za dodavanje na del od teloto ako izede zeleno jabolko
        nasoka = state[1]
        zeleni_jabolki = list(state[2])
        crveni_jabolki = list(state[3])
        br_zeleni = len(zeleni_jabolki)



        #ProdolzhiPravo
        if nasoka == "SEVER":
            if head_y + 1 < self.grid_size[1] and (head_x, head_y + 1) not in crveni_jabolki and (head_x,head_y + 1) not in body:
                new_body = body + [end] if body else [end]
                if (head_x,head_y + 1) in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Prodolzhi Pravo"] = (([(head_x, head_y + 1)] + body),nasoka,zeleni_jabolki,crveni_jabolki)
                else:
                    successors["Prodolzhi Pravo"] = (([(head_x, head_y + 1)] + body[:-1]), nasoka, zeleni_jabolki, crveni_jabolki)

        if nasoka == "JUG":
            if head_y - 1 >= 0 and (head_x, head_y - 1) not in crveni_jabolki and (head_x, head_y - 1) not in body:
                new_body = body + [end] if body else [end]
                if (head_x, head_y - 1) in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Prodolzhi Pravo"] = (([(head_x, head_y - 1)] + body),nasoka,zeleni_jabolki,crveni_jabolki)
                else:
                    successors["Prodolzhi Pravo"] = (([(head_x, head_y - 1)] + body[:-1]), nasoka, zeleni_jabolki, crveni_jabolki)


        if nasoka == "ZAPAD":
            if head_x - 1 >= 0 and (head_x - 1, head_y) not in crveni_jabolki and (head_x - 1, head_y) not in body:
                new_body = body + [end] if body else [end]
                if head_x - 1 >= 0 and (head_x - 1, head_y)  in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Prodolzhi Pravo"] = (([(head_x - 1, head_y)] + body),nasoka,zeleni_jabolki,crveni_jabolki)
                else:
                    successors["Prodolzhi Pravo"] = (([(head_x - 1, head_y)] + body[:-1]), nasoka, zeleni_jabolki, crveni_jabolki)

        if nasoka == "ISTOK":
            if head_x + 1 < self.grid_size[0] and (head_x + 1, head_y) not in crveni_jabolki and (head_x + 1, head_y)not in body:
                new_body = body + [end] if body else [end]
                if (head_x + 1, head_y) in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Prodolzhi Pravo"] = (([(head_x + 1,head_y)] + body),nasoka,zeleni_jabolki,crveni_jabolki)
                else:
                    successors["Prodolzhi Pravo"] = (([(head_x + 1,head_y)] + body[:-1]), nasoka, zeleni_jabolki, crveni_jabolki)


        # SvrtiDesno

        if nasoka == "SEVER":
            if head_y + 1 < self.grid_size[0] and (head_x + 1, head_y) not in crveni_jabolki and (head_x + 1, head_y) not in body:
                if (head_x + 1, head_y) in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Svrti Desno"] = (([(head_x + 1, head_y)] + body), 'ISTOK', zeleni_jabolki, crveni_jabolki)
                else:
                    successors["Svrti Desno"] = (([(head_x + 1, head_y)] + body[:-1]), "ISTOK", zeleni_jabolki, crveni_jabolki)

        if nasoka == "JUG":
            if head_x - 1 >= 0 and (head_x - 1, head_y) not in crveni_jabolki and (head_x - 1, head_y) not in body:
                if (head_x - 1, head_y) in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Svrti Desno"] = (([(head_x - 1, head_y)] + body), "ZAPAD", zeleni_jabolki, crveni_jabolki)
                else:
                    successors["Svrti Desno"] = (
                    ((int(head_x - 1), head_y), body), "ZAPAD", zeleni_jabolki, crveni_jabolki)

        if nasoka == "ZAPAD":
            if head_y + 1 < self.grid_size[0] and (head_x ,head_y + 1) not in crveni_jabolki and (head_x, head_y + 1) not in body:
                if (head_x, head_y + 1) in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Svrti Desno"] = (([(head_x, head_y + 1)] + body), "SEVER", zeleni_jabolki, crveni_jabolki)
                else:
                    successors["Svrti Desno"] = (([(head_x, head_y + 1)] + body[:-1]), "SEVER", zeleni_jabolki, crveni_jabolki)

        if nasoka == "ISTOK":
            if head_y - 1 >= 0 and (head_x, int(head_y - 1)) not in crveni_jabolki and (head_x, head_y - 1) not in body:
                if (head_x , head_y - 1) in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Svrti Desno"] = (([(head_x, head_y - 1)] + body), "JUG", zeleni_jabolki, crveni_jabolki)
                else:
                    successors["Svrti Desno"] = (([(head_x, head_y - 1)] + body[:-1]), "JUG", zeleni_jabolki, crveni_jabolki)

        # SvrtiLevo

        if nasoka == "SEVER":
            if head_x - 1 >= 0 and (head_x - 1, head_y) not in crveni_jabolki and (head_x - 1, head_y) not in body:
                new_body = body + [end] if body else [end]
                if (head_x - 1, head_y) in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Svrti Levo"] = (([(head_x - 1, head_y )] + body), 'ZAPAD', zeleni_jabolki, crveni_jabolki)
                else:
                    successors["Svrti Levo"] = (([(head_x - 1, head_y )] + body[:-1]), "ZAPAD", zeleni_jabolki, crveni_jabolki)

        if nasoka == "JUG":
            if head_x + 1 < self.grid_size[0]  and (head_x + 1, head_y) not in crveni_jabolki and (head_x + 1, head_y) not in body:
                if (head_x + 1, head_y) in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Svrti Levo"] = (([(head_x + 1, head_y )] + body), "ISTOK", zeleni_jabolki, crveni_jabolki)
                else:
                    successors["Svrti Levo"] = (([(head_x + 1, head_y )] + body[:-1]), "ISTOK", zeleni_jabolki, crveni_jabolki)

        if nasoka == "ZAPAD":
            if head_y - 1 >= 0 and (head_x , head_y - 1) not in crveni_jabolki and (head_x , head_y - 1) not in body:
                if (head_x, head_y - 1) in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Svrti Levo"] = (([(head_x, head_y - 1)] + body), "JUG", zeleni_jabolki, crveni_jabolki)
                else:
                    successors["Svrti Levo"] =(([(head_x, head_y - 1)] + body[:-1]), "JUG", zeleni_jabolki, crveni_jabolki)

        if nasoka == "ISTOK":
            if head_y + 1 < self.grid_size[0] and (head_x , head_y + 1) not in crveni_jabolki and (head_x , head_y + 1) not in body:
                if (head_x, head_y + 1) in zeleni_jabolki:
                    br_zeleni -= 1
                    successors["Svrti Levo"] = (([(head_x, head_y + 1)] + body), "SEVER", zeleni_jabolki, crveni_jabolki)
                else:
                    successors["Svrti Levo"] = (([(head_x, head_y + 1)] + body[:-1]), "SEVER", zeleni_jabolki, crveni_jabolki)


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0


if __name__ == '__main__':




    zeleni_jabolki = [(6, 9), (2, 7), (9, 5), (2, 3), (4, 3)]

    crveni_jabolki = [(4, 6), (6, 5), (3, 3), (6, 8)]

    ze = tuple(zeleni_jabolki)
    cr = tuple(crveni_jabolki)
    head =  (0, 7)
    body = ((0, 8), (0, 9))
    nasoka = "JUG"

    problem = Snake((((head[0], head[1]), body), nasoka, ze, cr))
    print(breadth_first_graph_search(problem).solution())


    # br_zeleni_jabolki = int(input())
    # zeleni_jabolki = []
    # for i in range (0,br_zeleni_jabolki):
    #     zeleni_jabolki.append([int(num) for num in input().split(",")])
    #
    # zeleni_jabolki = [tuple(zeleno) for zeleno in zeleni_jabolki]