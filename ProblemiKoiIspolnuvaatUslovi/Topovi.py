from constraint import *


def constraint (top1, top2):
    # dadeni se poziciite na topovite
    return top1[0] != top2[0] and top1[1] != top2[1]

if __name__ == '__main__':

    problem = Problem()

    #domenot ni se site polinja (redica, kolona)
    domain = [(i, j) for i in range(0,8) for j in range(0,8)]
    topovi = range(1,9)

    problem.addVariables(topovi,domain)

    for top1 in topovi:
        for top2 in topovi:
            if top1 != top2:
                problem.addConstraint(constraint, (top1, top2))


    solution = problem.getSolution()

    print(solution)

