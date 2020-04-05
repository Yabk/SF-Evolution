"""Module containing abstract class for learning models (individuals) and their factories"""
from abc import ABC, abstractmethod
from copy import deepcopy


class Individual(ABC):
    """Abstract individual class"""

    def __init__(self):
        """Initialize the individual"""
        self.fitness = 0

    @abstractmethod
    def evaluate(self, inputs):
        """Evaluate given imputs and return the outputs"""

    @abstractmethod
    def to_file(self, file_path):
        """Save the individual to a file"""

    @staticmethod
    @abstractmethod
    def from_file(file_path):
        """Load the individual from a file"""

    def copy(self):
        """Return a copy of self"""
        return deepcopy(self)


class IndividualGenerator(ABC):
    """Abstract individual factory class"""

    def __init__(self):
        """Initialize the hyperparameters for generated individuals"""

    @abstractmethod
    def generate(self):
        """Generate an individual using defined hyperparameters"""

    def batch_generate(self, individual_count):
        """Generate a batch of inidividuals"""
        return [self.generate() for _ in range(individual_count)]
