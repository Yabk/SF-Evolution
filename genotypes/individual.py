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

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __ge__(self, other):
        return self.fitness >= other.fitness

    def __le__(self, other):
        return self.fitness <= other.fitness

    def __str__(self):
        return str(self.fitness)


class IndividualGenerator(ABC):
    """Abstract individual factory class"""

    def __init__(self):
        """Initialize the hyperparameters for generated individuals"""

    @abstractmethod
    def generate(self, chromosome=None):
        """Generate an individual using predefined hyperparameters.

        :param chromosome: Use given chromosome value for new individual
                           Random if None.
        """

    def batch_generate(self, individual_count):
        """Generate a batch of inidividuals"""
        return [self.generate() for _ in range(individual_count)]
