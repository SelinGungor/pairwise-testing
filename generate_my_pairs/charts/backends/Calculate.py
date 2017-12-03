import charts.backends.TestOptimization as opt


class Calculate(object):
    def __init__(self, parameters):
        self.parameters = parameters

    def get_proposal_with_linear_programming(self, parameters):
        test_optimization = opt.TestOptimization(parameters)
        proposal = test_optimization.optimize_LP()
        print({k: v for k, v in proposal.items() if v})
        print('Number of tests', sum(proposal.values()))
        return proposal

    def get_proposal_with_simulated_annealing(self, parameters):
        test_optimization = opt.TestOptimization(parameters)
        proposal = test_optimization.optimize_simulated_annealing(inclusion_probability=0.45,
                                                                 exponential_shift=0.002,
                                                                 number_steps=5000)
        print({k: v for k, v in proposal.items() if v})
        print('Number of tests', sum(proposal.values()))
        return proposal