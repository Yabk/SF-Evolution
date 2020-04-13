"""Module contianing a test run of Genetic Algorithm and CGP in problem of symbolic regression"""
from selectors.roulette_wheel_selector import RouletteWheelSelector
from algorithms.genetic_algorithm import GeneticAlgorithm
from evaluators.math_function_evaluator import MathFunctionEvaluator
from reporters.useless_reporter import UselessReporter
from crossovers.point_crossover import PointCrossover
from mutations.cgp.smart_mutation import CGPSmartMutation
from genotypes.cgp.cgp import CGPGenerator


def main():
    """Run a symbolic regression on "x+y-z" expression using CGP and genetic algorithm"""
    evaluator = MathFunctionEvaluator('2*x+y-z', [(-1, -1, -1), (-2, -3, -1), (0, -1, 2),
                                                  (1, 3, -2), (-2, -1, 4), (2, 3, -1)])
    reporters = [UselessReporter()]
    selector = RouletteWheelSelector()

    input_len = 3
    grid_size = (3, 3)
    output_len = 1
    individual_generator = CGPGenerator(input_len, grid_size, output_len)

    crossover = PointCrossover(individual_generator, 2)
    mutation = CGPSmartMutation(n=4)
    population_size = 100
    max_iterations = 30

    alg = GeneticAlgorithm(reporters, evaluator, selector, crossover, mutation,
                           population_size, individual_generator, max_iterations)

    alg.run()


if __name__ == '__main__':
    main()
