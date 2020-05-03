"""Module containing learning algorithm abstract class"""
import os
import sys
from typing import Final
from abc import ABC, abstractmethod
from datetime import datetime
from signal import signal, SIGINT


class Algorithm(ABC):
    """Abstract learning algorithm class"""

    SAVED_POPULATIONS_DIR: Final = './saved_populations'

    def __init__(self, reporters, max_iterations, evaluator, individual_generator,
                 target_fitness=None):
        """Initialize hyperparameters for the algorithm.

        :param reporters: List of Reporter instances
        :param max_iterations: Max iterations of the algorithm
        :param evaluator: Evaluator instance
        :param individual_generator: Individual factory
        :param target_fitness: If an individual reaches target_fitness the algorithm is stopped.
                               If None, won't stop based on fitness.
        """
        self.reporters = reporters
        self.max_iterations = max_iterations
        self.evaluator = evaluator
        self.individual_generator = individual_generator
        self.target_fitness = target_fitness
        self.best_individual = None
        self.population = []
        self.iteration = 0

        def signal_handler(*args):
            print("Received SIGINT. Stopping the run and saving the current population.")
            self._save_population()
            sys.exit()

        signal(SIGINT, signal_handler)

    @abstractmethod
    def run(self):
        """Run the algorithm"""

    def _save_best_individual(self):
        """Save the best individual to file"""
        filename = datetime.today().isoformat()+'-'+self.__class__.__name__+'-'+\
                   self.best_individual.__class__.__name__+'.txt'
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


    def _check_iteration(self):
        """Increase iteration counter, check for new_best individual and stop condition

        :returns: stop condition boolean
        """
        self.iteration += 1
        if self.population[0].fitness > self.best_individual.fitness:
            self.best_individual = self.population[0]
            return self._stop_condition()
        return False


    def _save_population(self):
        """Save the current population to 'saved_populations' directory"""
        if not os.path.isdir(self.SAVED_POPULATIONS_DIR):
            os.mkdir(self.SAVED_POPULATIONS_DIR)
        save_dir = self.SAVED_POPULATIONS_DIR+'/'+\
                   datetime.today().isoformat()+'-'+self.__class__.__name__+'-'+\
                   self.individual_generator.individual_class.__name__+'/'
        os.mkdir(save_dir)
        for i, individual in enumerate(self.population, start=1):
            individual.to_file(save_dir+f'{i:04}')
