"""Module containing abstract reporter class.

The purpose of a reporter is to record the progression of an algorithm.
Algorithm will call the reporter periodically giving it a list of evaluated individuals.
For example, genetic algorithm might call the reporter after every generation is evaluated.
"""
from abc import ABC, abstractmethod


class Reporter(ABC):
    """Abstract reporter class"""

    def __init__(self):
        """Initialize the reporter"""

    @abstractmethod
    def report(self, individuals):
        """Report using given evaluated individuals"""
