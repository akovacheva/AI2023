from constraint import *

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    ...
    variables = list(papers.keys())
    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata

    ai_papers = [p for p in papers if papers[p] == 'AI']
for termin in domain:
    ai = [p for p in ai_papers if problem.getSolution()[p] == termin]
    if len(ai_papers) <= 4:
        problem.addConstraint(ai_papers, termin)


ai_papers = [p for p in papers if papers[p] == 'AI']
for termin in domain:
    ai = [p for p in ai_papers if problem.getSolution()[p] == termin]
    if len(ai) > 4:
        problem.addConstraint(AllDifferentConstraint(), ai)


result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje


names = sorted(result)
values = []
# for x in names:
#     values.append(result[x])

# s = papers.values()
# for val in s:
#     val

# for i in range(0, len(names)):
#     print(f'({val}) : {values[i]}')


for i in range(0, len(names)):
    print(f'{names.sort()[i]} ({[p for p in papers.values()][i]}): {values[i]}')


