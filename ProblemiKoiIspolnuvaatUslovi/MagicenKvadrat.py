from constraint import *

if __name__ == '__main__':

    problem = Problem()

    num = range(0, 16)
    domain = range(1,17)

    problem.addVariables(num, domain)

    #Constraints, na sekoe pole razlicen broj

    problem.addConstraint(AllDifferentConstraint(), num) #sekoe od polinjata, razlicna vrednost od domenot

    # Ista suma vo sekoja redica, kolona, dijagonala

    """
    00 01 02 03 
    04 05 06 07
    08 09 10 11
    12 13 14 15
    """

    for row in range(4):
        problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range(4)]) # -> (0,1,2,3) ,(4,5,6,7) ...  za site redici

    for col in range(4):
        problem.addConstraint(ExactSumConstraint(34),[col + 4 * i for i in range(4)]) # (0, 4, 8, 12)...

    # Za dijagonalite
    problem.addConstraint(ExactSumConstraint(34), range(0, 16, 5)) # so cekor 5
    problem.addConstraint(ExactSumConstraint(34), range(3, 13, 3)) # so cekor 3

    solution = problem.getSolution()
    print(solution)