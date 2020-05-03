"""Module contianing a test run of Evolution Strategy and CGP in problem of symbolic regression"""
from algorithms.evolution_strategy import EvolutionStrategy
from reporters.best_individual_reporter import BestIndividualReporter
from evaluators.math_function_evaluator import MathFunctionEvaluator
from mutations.cgp.smart_mutation import CGPSmartMutation
from genotypes.cgp.cgp import CGPIndividual
from genotypes.individual import IndividualGenerator


def main():
    """Run a symbolic regression on "x+y-z" expression using CGP and symbolic regression"""
    evaluator = MathFunctionEvaluator('x-8*y-z', [(-1, -1, 5), (-2, -3, 2), (0, -1, -123),
                                                  (1, 3, 5), (-2, -1, 0), (2, 3, 2)])
    reporters = [BestIndividualReporter()]

    cgp_hyperparams = {
        'input_len': 3,
        'grid_size': (3, 3),
        'output_len': 1,
        'constant_len': 4,
    }
    generator = IndividualGenerator(CGPIndividual, cgp_hyperparams)

    mutation = CGPSmartMutation(n=1)

    max_iterations = 0
    parent_count = 1
    children_count = 4
    alg = EvolutionStrategy(reporters, max_iterations, evaluator, generator,
                            parent_count, children_count, mutation, elitism=True, target_fitness=0)

    alg.run()


if __name__ == '__main__':
    main()
