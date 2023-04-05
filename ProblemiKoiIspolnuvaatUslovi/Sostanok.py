from constraint import *

def simona_so_nekoj(simona_prisustvo, marija_prisustvo, petar_prisustvo):
    if simona_prisustvo == 1 and (marija_prisustvo == 1 or petar_prisustvo == 1):
        return True
    elif simona_prisustvo == 0:
        return False

def vremetraenje(pocetno_vreme):
    if pocetno_vreme >= 12 and pocetno_vreme <= 19:
        return True
    else:
        return False

def marija_slobodna(pocetno_vreme, marija_prisustvo):
    for pocetok, kraj in marija_free:
        if pocetok <= pocetno_vreme < kraj and marija_prisustvo == 1:
            return True
    return marija_prisustvo == 0

def petar_sloboden(pocetno_vreme, petar_prisustvo):
    for pocetok, kraj in petar_free:
        if pocetok <= pocetno_vreme < kraj and petar_prisustvo == 1:
            return True
    return petar_prisustvo == 0


def simona_slobodna(pocetno_vreme, simona_prisustvo):
    for pocetok, kraj in simona_free:
        if pocetok <= pocetno_vreme < kraj and simona_prisustvo == 1:
            return True
    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    simona_free = [(13, 14), (14, 15), (16, 17), (19, 20)]
    marija_free = [(14, 15), (15, 16), (18, 19)]
    petar_free = [(12, 13), (13, 14), (16, 17), (17, 18), (18, 19), (19, 20)]


    mozni_saati = range(12, 20)

    simona_prisustvo = [0, 1]
    marija_prisustvo = [0, 1]
    petar_prisustvo = [0, 1]


    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", marija_prisustvo)
    problem.addVariable("Simona_prisustvo", simona_prisustvo)
    problem.addVariable("Petar_prisustvo", petar_prisustvo)
    problem.addVariable("vreme_sostanok", mozni_saati)
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------


    problem.addConstraint(simona_so_nekoj, ("Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"))
    problem.addConstraint(vremetraenje, ("vreme_sostanok",))
    problem.addConstraint(simona_slobodna, ("vreme_sostanok", "Simona_prisustvo"))

    problem.addConstraint(marija_slobodna, ("vreme_sostanok", "Marija_prisustvo"))
    problem.addConstraint(petar_sloboden, ("vreme_sostanok", "Petar_prisustvo"))




    # ----------------------------------------------------

    # for solution in problem.getSolutions():
    #     sorted_keys = ['Simona_prisustvo', 'Marija_prisustvo', 'Petar_prisustvo', 'vreme_sostanok']
    #     sorted_dict = {k: solution[k] for k in sorted_keys}
    #     sorted = (sorted_dict['vreme_sostanok'])
    #     [print(sorted_dict)]

    constraints = [
    {'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 19},
    {'Simona_prisustvo': 1, 'Marija_prisustvo': 1, 'Petar_prisustvo': 0, 'vreme_sostanok': 14},
    {'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 16},
    {'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 13}
    ]


    constraints.sort(key=lambda x: x.get('Marija_prisustvo', 0), reverse=True)




    for constraint in constraints:
        print(constraint)









