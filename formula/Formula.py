from itertools import chain, combinations, product

class getFormula:

    def formula(self):
        agents = {
            'a1': ['a2', 'a3', 'a5'],
            'a2': ['a1', 'a3', 'a4'],
            'a3': ['a1', 'a2', 'a5'],
            'a4': ['a2'],
            'a5': ['a1', 'a3'],
            'a6': []
        }
        pairs = {(k, v) for k in agents for v in agents[k]}
        return pairs


formula = getFormula()

print(formula.formula())

class getPairs:

    def pairwiseGen(*sequences):
        unseen = set(chain.from_iterable(product(*i) for i in combinations(sequences, 2)))
        for path in product(*sequences):
            common_pairs = set(combinations(path, 2)) & unseen
            print(common_pairs)
            if common_pairs:
                yield path
                unseen.difference_update(common_pairs)

parameters = [ [ "Brand X", "Brand Y","Brand A","Brand B","Brand C","Brand D" ]
                 , [ "98", "NT", "2000", "XP"]
                 , [ "Internal", "Modem","A","B","C","D","E","F","G","H","I","J","K","L","M" ]
                 , [ "Salaried", "Hourly", "Part-Time", "Contr.","AA","BB","CC","DD","EE","FF","GG","HH","II" ]
                 , [ 6, 10, 15, 30, 60, 70, 80, 90, 100, 110, 120, 130, 140 ]
                 ]

pairs = getPairs()

print(list(pairs.pairwiseGen(*parameters)))