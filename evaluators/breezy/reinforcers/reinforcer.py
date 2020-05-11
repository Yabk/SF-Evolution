"""Module containing Reinforcer abstract class"""
from abc import ABC, abstractmethod


class Reinforcer(ABC):
    """Abstract Reinforcer class"""

    @abstractmethod
    def update(self, features, action):
        """Observer method

        :param features: features that individual received
        :param action: action that individual made
        """

    @abstractmethod
    def end(self, data):
        """Return fitness won.
        This method marks an end of a run for current individual.
        """
