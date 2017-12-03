import numpy as np
import itertools
from collections import defaultdict
import copy
import pulp


class TestOptimization(object):
    def __init__(self, parameters):
        self.parameters = parameters
        self.combinations = self.create_combinations(parameters)
        self.pairs = self.create_pairs(parameters)
        self.pairs_in_combinations = self.create_pairs_in_combinations()

    # Initialize proposal for Simmulated Annealing, retry sampling until we find a valid initial solution
    def initial_proposal(self, inclusion_probability=0.5):
        counter = 0
        while True:
            counter += 1
            proposal = {c: np.random.rand() < inclusion_probability for c in self.combinations}
            if self.contains_all_pairs(proposal):
                print('Initial proposal after {} times'.format(counter))
                return proposal

    # Get a list of all possible combinations of parameters
    def create_combinations(self, parameters):
        return list(itertools.product(*parameters))

    # Create dictionary with 'pair' tuple as key and a list of all combinations that include this pair
    def create_pairs_in_combinations(self):
        pairs_dict = defaultdict(list)
        for combination in self.combinations:
            for pair in itertools.combinations(combination, 2):
                pairs_dict[pair].append(combination)
        return pairs_dict

    # Create a list of all possible pairs of parameters
    def create_pairs(self, parameters):
        pairs = []
        for parameter_1 in range(len(parameters) - 1):
            for parameter_2 in range(parameter_1 + 1, len(parameters)):
                pairs.extend(list(itertools.product(parameters[parameter_1], parameters[parameter_2])))
        return pairs

        # Check if our proposal contains all the possible pairs

    def contains_all_pairs(self, proposal):
        for pair in self.pairs:
            if not any([proposal[combination] for combination in self.pairs_in_combinations[pair]]):
                return False
        return True

    # Given our current proposal, create a list of all proposals where one test is added or removed,
    # but only the ones that remain valid
    def create_neighborhood(self, proposal):
        neighborhood = []
        for key in proposal.keys():
            new_proposal = copy.copy(proposal)
            new_proposal[key] = not new_proposal[key]
            if self.contains_all_pairs(new_proposal):
                neighborhood.append(new_proposal)
        return neighborhood

    # Calculate energy of our proposal, in this case just the amount of tests in there, lower is better
    def energy(self, proposal):
        return sum(proposal.values())

    # Given the energy of our current proposal, the potential proposal and the temperature, see if we go to the new proposal
    def go_to_potential(self, current_energy, potential_energy, temperature):
        if current_energy >= potential_energy:
            return True
        prob = temperature
        if prob > np.random.rand():
            return True
        return False

    # Create the neighborhood of our current proposal, sample from it and see if we move to the new proposal
    def sample_neighborhood(self, proposal, temperature):
        neighborhood = self.create_neighborhood(proposal)
        current_energy = self.energy(proposal)
        potential_proposal = np.random.choice(neighborhood)
        potential_energy = self.energy(potential_proposal)
        if self.go_to_potential(current_energy, potential_energy, temperature):
            return potential_proposal, potential_energy
        return proposal, current_energy

    # Find solution using simulated annealing, temperature lowers with an exponential rate, number_steps is the amount
    # of steps taken until the temperature reaches 0 and the optimization stops
    def optimize_simulated_annealing(self, inclusion_probability=0.5, number_steps=5000, exponential_shift=0.001):
        proposal = self.initial_proposal(inclusion_probability)
        step_size = - np.log(exponential_shift) / number_steps
        best_proposal = None
        best_energy = 10000000
        iterations = 0
        temperature = 1.
        while temperature >= 0.:
            temperature = np.exp(-step_size * iterations) - exponential_shift
            iterations += 1
            proposal, energy = self.sample_neighborhood(proposal, temperature)
            if energy < best_energy:
                best_energy = energy
                best_proposal = proposal
            if iterations % 10 == 0:
                print(iterations, temperature, energy)
        return best_proposal

    # Optimization using Linear Programming
    def optimize_LP(self):
        problem = pulp.LpProblem('Pairwise Testing problem', pulp.LpMinimize)
        combination_decisions = {combo: pulp.LpVariable(combo, 0, 1, pulp.LpBinary) for combo in self.combinations}
        problem += sum(combination_decisions.values())
        for pair in self.pairs_in_combinations:
            combinations_in_pair = self.pairs_in_combinations[pair]
            problem += sum([combination_decisions[combo] for combo in combinations_in_pair]) >= 1
        problem.solve()

        solution = {}

        for combo in TestOptimization.combinations:
            if pulp.value(combination_decisions[combo]) > 0.5:
                solution[combo] = True
            else:
                solution[combo] = False
        return solution