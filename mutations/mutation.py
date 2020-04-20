"""Module containing mutation abstract class"""
from abc import ABC, abstractmethod


class Mutation(ABC):
    """Abstract mutation class"""

    def __init__(self):
        """Initialize the mutation"""

    @abstractmethod
    def mutate(self, individual):
        """Mutate given individual"""

    def batch_mutate(self, individuals):
        """Mutate given group of individuals"""
        for individual in individuals:
            self.mutate(individual)
