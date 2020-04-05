"""Module containing evaluator abstract class"""
from abc import ABC, abstractmethod


class Evaluator(ABC):
    """Abstract evaluator class"""

    def __init__(self):
        """Initialize the evaluator"""
        self.input_len = 0
        self.output_len = 0

    @abstractmethod
    def evaluate(self, individual):
        """Evaluate a single individual"""

    @abstractmethod
    def batch_evaluate(self, individuals):
        """Evaluate a batch of individuals and sort them by fitness in descending order"""
