from constraint import *

# Promenlivi:  WA, NT, Q, NSW, V, SA, T
#Domen:  crvena, zelena, sina
#Ogranicuvanje: sosednite regioni mora da imaat razlicni boi


#Pomosna funkcija za ogranicuvanjata
def different(a,b):
    return a != b


if __name__ == '__main__':
    problem = Problem()

    variables = ["WA", "NT", "Q", "NSW", "V", "SA", "T"]
    domain = ["red", "green", "blue"]

    #Posto site promenlivi imaat ist domen
    problem.addVariables(variables, domain)

    #Dodavanje ogranicuvanja - spored mapata
    problem.addConstraint(different, ("WA","NT"))
    problem.addConstraint(different, ("WA","SA"))
    problem.addConstraint(different, ("NT","SA"))
    problem.addConstraint(different, ("NT","Q"))
    problem.addConstraint(different, ("SA","Q"))
    problem.addConstraint(different, ("SA","NSW"))
    problem.addConstraint(different, ("SA","V"))
    problem.addConstraint(different, ("NSW","V"))
    problem.addConstraint(different, ("NSW","Q"))

    solutions = problem.getSolutions()

    print(solutions)
