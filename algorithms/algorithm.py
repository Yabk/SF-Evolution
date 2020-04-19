"""Module containing learning algorithm abstract class"""
import os
from abc import ABC, abstractmethod
from datetime import datetime


class Algorithm(ABC):
    """Abstract learning algorithm class"""

    def __init__(self, reporters, max_iterations, target_fitness=None):
        """Initialize hyperparameters for the algorithm.

        :param reporters: List of Reporter instances
        :param max_iterations: Max iterations of the algorithm
        :param target_fitness: If an individual reaches target_fitness the algorithm is stopped.
                               If None, won't stop based on fitness.
        """
        self.reporters = reporters
        self.max_iterations = max_iterations
        self.target_fitness = target_fitness
        self.best_individual = None
        self.population = []

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


    def _stop_condition(self):
        return False if self.target_fitness is None  \
                     else self.best_individual.fitness >= self.target_fitness
