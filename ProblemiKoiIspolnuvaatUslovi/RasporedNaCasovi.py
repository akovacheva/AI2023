from constraint import *


def proverka(predavanje, vezbi):
    for p in ML_predavanja_domain:
        for v in ML_vezbi_domain:
            if p[-2:] == v[-2:]:
                if predavanje == p and vezbi == v:
                    return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------

    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    for i in casovi_ML:
        problem.addVariable(f"ML_cas_{i}", ML_predavanja_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    for i in casovi_AI:
        problem.addVariable(f"AI_cas_{i}", AI_predavanja_domain)
    for i in casovi_BI:
        problem.addVariable(f"BI_cas_{i}", BI_predavanja_domain)
    for i in casovi_R:
        problem.addVariable(f"R_cas_{i}", R_predavanja_domain)

    daysAI = [x[3:] for x in AI_predavanja_domain]
    timesAI = [x[-2:] for x in AI_predavanja_domain]

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint())

    problem.addConstraint(proverka, ("ML_cas_1", "ML_vezbi"))

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
