"""Module containing learning algorithm abstract class"""
import os
from abc import ABC, abstractmethod
from datetime import datetime


class Algorithm(ABC):
    """Abstract learning algorithm class"""

    def __init__(self, reporters):
        """Initialize hyperparameters for the algorithm"""
        self.best_individual = None
        self.population = []
        self.reporters = reporters

    @abstractmethod
    def run(self):
        """Run the algorithm"""

    def _save_best_individual(self):
        """Save the best individual to file"""
        filename = datetime.today().isoformat()+'-'+self.__class__.__name__+'.txt'
        try:
            self.best_individual.to_file('./best_individuals/'+filename)
        except FileNotFoundError:
            os.mkdir('./best_individuals/')
            self.best_individual.to_file('./best_individuals/'+filename)


    def _report(self):
        for reporter in self.reporters:
            reporter.report(self.population)
