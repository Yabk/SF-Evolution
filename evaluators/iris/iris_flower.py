"""Module containing evaluator for Iris flower clasificator.
It uses famous Ronald Fisher's dataset."""
from os.path import dirname, join
from ..evaluator import Evaluator


class IrisFlowerEvaluator(Evaluator):
    """Iris Flower Classification Evaluator"""

    def __init__(self):
        """Initialize the evaluator"""
        super().__init__(4, 3)

        with open(join(dirname(__file__), 'iris.csv'), 'r') as dataset_file:
            self.dataset = [[float(x) for x in line.rstrip().split(',')]
                            for line in dataset_file.readlines()]

    def evaluate(self, individual):
        """Evaluate the individual on the whole dataset"""
        fitness = 0
        for datapoint in self.dataset:
            output = individual.evaluate(datapoint[:-1])
            result = output.index(max(output))
            if result == datapoint[-1]:
                fitness += 1

        individual.fitness = fitness
