from constraint import *

def differentRowColumn(q1,q2):
    return q1[0] != q2[0] and q1[1] != q2[1]

def notInDiagonal(q1, q2):
    return abs(q1[0] - q2[0]) != abs(q1[1] - q2[1])

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    queens = range(1, n + 1)
    tabla = [(x, y) for x in range(n) for y in range(n)]

    problem.addVariables(queens, tabla)

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(), Domain(queens))

    for q1 in queens:
        for q2 in  queens:
            if q1 == q2:
                continue
            else:
                problem.addConstraint(differentRowColumn, (q1, q2))
                problem.addConstraint(notInDiagonal, (q1, q2))

    # ----------------------------------------------------


    if n <= 6:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())