"""Module containing evaluator abstract class"""
from abc import ABC, abstractmethod


class Evaluator(ABC):
    """Abstract evaluator class"""

    def __init__(self, input_len, output_len):
        """Initialize the evaluator"""
        self.input_len = input_len
        self.output_len = output_len

    @abstractmethod
    def evaluate(self, individual):
        """Evaluate a single individual"""

    def batch_evaluate(self, individuals):
        """Evaluate a batch of individuals and sort them by fitness in descending order"""
        for individual in range(len(individuals)):
            self.evaluate(individual)
        individuals.sort(key=lambda individual: individual.fitness, reverse=True)
