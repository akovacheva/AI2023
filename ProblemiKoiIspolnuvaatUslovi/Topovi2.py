from constraint import *

#Poefikasno resenie, topovite gi ko0ristime kako brojka koloni i gi sporeduvam eos redici, da ne bidat na istite


if __name__ == '__main__':

    problem = Problem()

    domain = range(0,8) #namesto 64 vrednosti, imame 8

   #columns
    rooks = range(0,8)

    problem.addVariables(rooks, domain)

    # #da ne se vo ista redica
    # for rook1 in rooks:
    #     for rook2 in rooks:
    #         if rook1 < rook2:
    #             problem.addConstraint(lambda r1,r2: r1 != r2, (rook1, rook2)) # da imaat razlicna redica
    #

    problem.addConstraint(AllDifferentConstraint())  #samo so ova odma se resava

    solution = problem.getSolution()
    print(solution)