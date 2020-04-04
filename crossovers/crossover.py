"""Module containing crossover abstract class"""
from abc import ABC, abstractmethod


class Crossover(ABC):
    """Crossover abstract class"""

    def __init__(self):
        """Initialize the crossover"""

    @abstractmethod
    def cross(self, individual_1, indvidual_2):
        """Return a list of child individual(s) using two given individuals as parents

        :param individual_1: first parent
        :param individual_2: second parent

        :returns: a list of children (even if only one child)
        """
