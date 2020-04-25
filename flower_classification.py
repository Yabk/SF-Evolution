"""Module contianing a test run of Evolution Strategy and Neural Network
in problem of Iris flower classification
"""
from algorithms.evolution_strategy import EvolutionStrategy
from reporters.best_individual_reporter import BestIndividualReporter
from evaluators.iris.iris_flower import IrisFlowerEvaluator
from mutations.nn.normal_mutation import NNNormalMutation
from genotypes.nn.nn import NNGenerator
from genotypes.nn.activation_functions import sigmoid


def main():
    """Run a classification test run on iris dataset"""
    evaluator = IrisFlowerEvaluator()

    reporters = [BestIndividualReporter()]

    layers = (4, 6, 3)
    activation_functions = (sigmoid, sigmoid)

    individual_generator = NNGenerator(layers, activation_functions)

    mutation = NNNormalMutation(stddev=0.05)

    max_iterations = 0
    parent_count = 50
    children_count = 200
    alg = EvolutionStrategy(reporters, max_iterations, evaluator,
                            individual_generator, parent_count,
                            children_count, mutation, elitism=True, target_fitness=148)

    alg.run()


if __name__ == '__main__':
    main()
