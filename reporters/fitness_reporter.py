"""Module containing Reporter implementation that reports whenever there is a new best individual"""
from sys import float_info
from .reporter import Reporter

class FitnessReporter(Reporter):
    """Fitness Reporter class"""

    def __init__(self, start_at=-float_info.max):
        """IInitialize the reporter

        :param start_at: Starting fitness
        """
        super().__init__()
        self.current = start_at

    def report(self, individuals):
        """Report if there is new best individual"""
        if individuals[0].fitness > self.current:
            self.current = individuals[0].fitness
            print(f'Current best: {self.current}')
