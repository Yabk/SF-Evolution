"""Module containing a test run of Genetic Algorithm and Neural Network
in problem of Iris flower classification
"""
from selectors.roulette_wheel_selector import RouletteWheelSelector
from reporters.best_individual_reporter import BestIndividualReporter
from evaluators.iris.iris_flower import IrisFlowerEvaluator
from mutations.nn.normal_mutation import NNNormalMutation
from genotypes.nn.nn import NNGenerator
from genotypes.nn.activation_functions import sigmoid
from crossovers.nn_point_crossover import NNPointCrossover
from algorithms.genetic_algorithm import GeneticAlgorithm


def main():
    """Run a classification test run on iris dataset"""
    evaluator = IrisFlowerEvaluator()

    layers = (4, 6, 3)
    activation_functions = (sigmoid, sigmoid)
    individual_generator = NNGenerator(layers, activation_functions)

    reporters = [BestIndividualReporter()]
    selector = RouletteWheelSelector()
    crossover = NNPointCrossover(individual_generator, 3)
    mutation = NNNormalMutation(stddev=0.03)

    population_size = 100
    max_iterations = 0
    target_fitness = 148

    alg = GeneticAlgorithm(reporters, evaluator, selector, crossover, mutation, population_size,
                           individual_generator, max_iterations, target_fitness=target_fitness)

    alg.run()


if __name__ == '__main__':
    main()
