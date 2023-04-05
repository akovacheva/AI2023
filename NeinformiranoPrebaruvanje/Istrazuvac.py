# Задача 1 - Истражувач
# Предложете соодветна репрезентација и напишете ги потребните функции во Python за да се реши следниот проблем за кој една можна почетна состојба е прикажана на сликата
#
# Потребно е човечето безбедно да дојде до куќичката. Човечето може да се придвижува на кое било соседно поле хоризонтално или вертикално.
# Пречките 1 и 2 се подвижни, при што и двете пречки се движат вертикално.
# Секоја од пречките се придвижува за едно поле во соодветниот правец и насока со секое придвижување на човечето.
# Притоа, пречката 1 на почетокот се движи надолу, додека пречката 2 на почетокот се движи нагоре.
# Пример за положбата на пречките после едно придвижување на човечето надесно е прикажан на десната слика.
#
#
# Кога некоја пречка ќе дојде до крајот на таблата при што повеќе не може да се движи во насоката во која се движела,
# го менува движењето во спротивната насока. Доколку човечето и која било од пречките се најдат на исто поле човечето ќе биде уништено.
# За сите тест примери изгледот и големината на таблата се исти како на примерот даден на сликите.
# За сите тест примери почетните положби, правец и насока на движење за препреките се исти. За секој тест пример почетната позиција на
# човечето се менува, а исто така се менува и позицијата на куќичката.
# Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример.
# Движењата на човечето потребно е да ги именувате на следниот начин:
# * Right- за придвижување на човечето за едно поле надесно
# * Left- за придвижување на човечето за едно поле налево
# * Up- за придвижување на човечето за едно поле нагоре
# * Down- за придвижување на човечето за едно поле надолу
# Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите секвенцата на движења
# која човечето треба да ја направи за да може од својата почетна позиција да стигне до позицијата на куќичката.
# Треба да примените неинформирано пребарување. Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.


from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

        #ja definirame goleminata na tablata
        self.grid_size = [8, 6]


    def successor(self, state):
        successors = dict()
        # n=-1 -> dole  n=1 -> gore
        #(x,y, (x_p1,y_p1,n_p1), (x_p2,y_p2,n_p2))

        man_x = state[0]
        man_y = state[1]

        #Gi pretvorame vo listi so cel da moze da im ja menuvame sostojbata
        precka1 = list(state[2])
        precka2 = list(state[3])

    # ZA PRECKITE
        if precka1[2] == 1: #up
            if precka1[1] == self.grid_size[1] - 1 :
                precka1[2] = -1
                precka1[1] -= 1
            else:
                precka1[1] += 1
        else:
            if precka1[1] == 0:
                precka1[2] == 1
                precka1[1] += 1
            else:
                precka1[1] -= 1

        if precka2[2] == 1: #up
            if precka2[1] == self.grid_size[1] - 1 :
                precka2[2] = -1
                precka2[1] -= 1
            else:
                precka2[1] += 1
        else:
            if precka2[1] == 0:
                precka2[2] == 1
                precka2[1] += 1
            else:
                precka2[1] -= 1


        precki = [(precka1[0],precka1[1]),(precka2[0],precka2[1])]
    # ZA COVECETO

        #   desno

        if man_x + 1 < self.grid_size[0] and  (man_x +1, man_y) not in precki :
            successors["Right"] = (man_x + 1, man_y,(precka1[0],precka1[1],precka1[2]),
                                   (precka2[0],precka2[1],precka2[2]))

        #   levo
        if man_x > 0 and  (man_x - 1, man_y) not in precki :
            successors["Left"] = (man_x - 1, man_y,(precka1[0],precka1[1],precka1[2]),
                                   (precka2[0],precka2[1],precka2[2]))
        #  gore

        if man_y + 1 < self.grid_size[0] and  (man_x, man_y + 1) not in precki :
            successors["Up"] = (man_x, man_y + 1,(precka1[0],precka1[1],precka1[2]),
                                   (precka2[0],precka2[1],precka2[2]))

        # dolu
        if man_y > 0 and  (man_x, man_y - 1) not in precki :
            successors["Down"] = (man_x, man_y - 1,(precka1[0],precka1[1],precka1[2]),
                                   (precka2[0],precka2[1],precka2[2]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]


if __name__ == '__main__':
    goal_state = (7,4)
    initial_state = (0,2)
    precka1 = (2,5,-1)
    precka2 = (5,0,1)

    explorer = Explorer((initial_state[0],initial_state[1], precka1, precka2), goal_state)

    print(breadth_first_graph_search(explorer).solution())