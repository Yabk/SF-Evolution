"""Module containing crossover abstract class"""
from abc import ABC, abstractmethod


class Crossover(ABC):
    """Crossover abstract class"""

    def __init__(self, individual_generator):
        """Initialize the crossover

        :param individual_generator: Generator that will be used to generate children
        """
        self.individual_generator = individual_generator

    @abstractmethod
    def cross(self, parent_1, parent_2):
        """Return a list of child individual(s) using two given individuals as parents

        :param parent_1: first parent
        :param parent_2: second parent

        :returns: a list of children (even if only one child)
        """
