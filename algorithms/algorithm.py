"""Module containing absract class for learning algorithm"""
from abc import ABC, abstractmethod


class Algorithm(ABC):
    """Abstract learning algorithm class"""

    def __init__(self):
        """Initialize hyperparameters for the algorithm"""

    @abstractmethod
    def run(self):
        """Run the algorithm"""
