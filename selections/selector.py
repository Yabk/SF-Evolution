"""Module containing Selector abstract class"""
from abc import ABC, abstractmethod


class Selector(ABC):
    """Abstract selector class"""

    def __init__(self):
        """Initialize the selector"""

    @abstractmethod
    def select(self, individuals, not_same_as=None):
        """Return a selected individual from a sorted list of individuals
        that is not the same as not_same_as individual

        :param individuals: group of individuals, sorted by fitness
                            in descending order, to select from
        :param not_same_as: selected individual should not be the same as this individual
        """
