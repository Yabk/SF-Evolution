"""Module contianing a test run of Evolution Strategy and CGP in problem of symbolic regression"""
from algorithms.evolution_strategy import EvolutionStrategy
from reporters.best_individual_reporter import BestIndividualReporter
from evaluators.math_function_evaluator import MathFunctionEvaluator
from mutations.cgp.smart_mutation import CGPSmartMutation
from genotypes.cgp.cgp import CGPGenerator


def main():
    """Run a symbolic regression on "x+y-z" expression using CGP and symbolic regression"""
    evaluator = MathFunctionEvaluator('x-8*y-z', [(-1, -1, 5), (-2, -3, 2), (0, -1, -123),
                                                  (1, 3, 5), (-2, -1, 0), (2, 3, 2)])
    reporters = [BestIndividualReporter()]

    input_len = 3
    grid_size = (3, 3)
    output_len = 1
    individual_generator = CGPGenerator(input_len, grid_size, output_len, 4)

    mutation = CGPSmartMutation(n=1)

    max_iterations = 0
    parent_count = 1
    children_count = 4
    alg = EvolutionStrategy(reporters, max_iterations, evaluator, individual_generator,
                            parent_count, children_count, mutation, elitism=True, target_fitness=0)

    alg.run()


if __name__ == '__main__':
    main()
