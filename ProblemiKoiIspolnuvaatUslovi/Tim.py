from constraint import *


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # n1 = int(input())
    # clenovi = [f'{input()}' for n1 in range(n1)]
    #
    # n2 = int(input())
    # lideri = [f'{input()}' for n2 in range(n2)]

    clenovi = ['31.3 A', '28.4 B', '26.1 C', '24.2 D', '21.8 E', '20.3 F', '15.5 G', '14.1 H', '12.5 I', '11.5 J']

    lideri = ['32.2 K', '27.4 L', '24.6 M', '14.9 N', '13.2 O']

    domainClenovi = [d[-1] for d in clenovi]
    domainLideri = [d[-1] for d in lideri]

    problem.addVariables([f'Participant {i}' for i in range(1, 10)], domainClenovi)
    # problem.addVariables([f'Participant {i}' for i in range(1, n1)], domainClenovi)
    problem.addVariable('Team leader', domainLideri)

    teziniClenovi = [float(t[:4]) for t in clenovi]
    teziniLideri = [float(t[:4]) for t in lideri]


    #Constraints
    problem.addConstraint(AllDifferentConstraint())

    # print(problem.getSolution())

    solution = problem.getSolution()
    print(f'Team leader: {solution["Team leader"]}')
    for i in range(1, 6):
        print(f'Participant {i}: {solution[f"Participant {i}"]}')

# Потсетник: Во дадениот модул constraint веќе се имплементирани следните ограничувања како класи:
# AllDifferentConstraint, AllEqualConstraint, MaxSumConstraint, ExactSumConstraint,  MinSumConstraint, InSetConstraint, NotInSetConstraint,
# SomeInSetConstraint,  SomeNotInSetConstraint.