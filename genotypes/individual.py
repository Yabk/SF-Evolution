"""Module containing abstract class for learning models (individuals) and their factories"""
from os import listdir
from os.path import isfile, join
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


class IndividualGenerator():
    """Individual factory class"""

    def __init__(self, individual_class, hyperparameters, population_path=None):
        """Initialize the generator

        :individual_class: class of an Individual that this generator will create
        :hyperparameters: hyperparamters for the generated individuals
        :population_path: path to a directory containing saved individuals
        """
        self.individual_class = individual_class
        self.hyperparameters = hyperparameters
        self.population = []
        if population_path is not None:
            self._load_population(population_path)


    def generate(self, chromosome=None):
        """Generate an individual using predefined hyperparameters.

        :param chromosome: Use given chromosome value for new individual
                           Random if None.
        """
        if self.population and chromosome is None:
            return self.population.pop(0)
        return self.individual_class(**self.hyperparameters, chromosome=chromosome)

    def batch_generate(self, individual_count):
        """Generate a batch of inidividuals"""
        return [self.generate() for _ in range(individual_count)]


    def _load_population(self, population_path):
        files = sorted([join(population_path, f) for f in listdir(population_path)
                        if isfile(join(population_path, f))])

        for f in files:
            self.population.append(self.individual_class.from_file(f))
