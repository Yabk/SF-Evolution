"""Module containing mutation abstract class"""
from abc import ABC, abstractmethod


class Mutation(ABC):
    """Abstract mutation class"""

    def __init__(self):
        """Initialize the mutation"""

    @abstractmethod
    def mutate(self, individual):
        """Mutate given individual"""
