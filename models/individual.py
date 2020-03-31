"""Module containing abstract class for learning models - individuals"""
from abc import ABC, abstractmethod
from copy import deepcopy


class Individual(ABC):
    """Abstract individual class"""

    def __init__(self):
        """Initialize the individual"""
        self.fitness = 0

    @abstractmethod
    def evaluate(self, values):
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
