from constraint import *

if __name__ == '__main__':

    problem = Problem()

    knights = range(0,8)
    domain = [(i,j) for i in range(8) for j in range(8)]

    problem.addVariables(knights, domain)

    problem.addConstraint(AllDifferentConstraint())

    solution = problem.getSolution()

    print(solution)
