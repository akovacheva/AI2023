from constraint import *


def MlCheck(p1, p2):
    return p1[-2:] != p2[-2:]

def allCheck(p1, p2):
    #"Mon_11"
    day1 = p1[:3]
    day2 = p2[:3]
    time1 = int(p1[-2:])
    time2 = int(p2[-2:])
    return day1 != day2 or abs(time1 - time2) >= 2



if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    AI_predavanja = []
    R_predavanja = []
    BI_predavanja = []
    ML_predavanja = []

    for i in range(1, casovi_ML+1):
        ML_predavanja.append(f'ML_cas_{i}')

    for i in range(1, casovi_AI+1):
        AI_predavanja.append(f'AI_cas_{i}')

    for i in range(1, casovi_R + 1):
        R_predavanja.append(f'R_cas_{i}')
    for i in range(1, casovi_BI+1):
        BI_predavanja.append(f'BI_cas_{i}')

# morashe vaka da se podelat za da moze da gi pristapam site za da stavam takov constraint
    problem.addVariables(AI_predavanja, Domain(AI_predavanja_domain))
    problem.addVariables(ML_predavanja, Domain(ML_predavanja_domain))
    problem.addVariables(R_predavanja, Domain(R_predavanja_domain))
    problem.addVariables(BI_predavanja, Domain(BI_predavanja_domain))
    problem.addVariable('AI_vezbi', Domain(AI_vezbi_domain))
    problem.addVariable('ML_vezbi', Domain(ML_vezbi_domain))
    problem.addVariable('BI_vezbi', Domain(BI_vezbi_domain))

    site = AI_predavanja + ML_predavanja + R_predavanja + BI_predavanja + ['AI_vezbi', 'ML_vezbi', 'BI_vezbi']
  # print(site)
    # ---Tuka dodadete gi ogranichuvanjata----------------
    for p1 in site:
        for p2 in site:
            if p1 == p2:
                continue
            problem.addConstraint(allCheck,(p1,p2))

    for p1 in [t for t in site if t[:2] == "ML"]:
        for p2 in [t for t in site if t[:2] == "ML"]:
            if p1 == p2:
                continue

            problem.addConstraint(MlCheck, (p1, p2))


    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)