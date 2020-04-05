"""Module containing learning algorithm abstract class"""
from abc import ABC, abstractmethod
from datetime import datetime


class Algorithm(ABC):
    """Abstract learning algorithm class"""

    def __init__(self):
        """Initialize hyperparameters for the algorithm"""
        self.best_individual = None

    @abstractmethod
    def run(self):
        """Run the algorithm"""

    def save_best_individual(self):
        """Save the best individual to file"""
        filename = datetime.today().isoformat()+'-'+self.__class__.__name__+'.txt'
        self.best_individual.to_file('./best_individuals/'+filename)
