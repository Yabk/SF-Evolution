"""Module containing Reporter implementation that reports average fitness of given individuals"""
from .reporter import Reporter

class FitnessReporter(Reporter):
    """Fitness Reporter class"""

    def report(self, individuals):
        """Report the average fitness of given group of individuals"""
        average_fitness = sum(individual.fitness for individual in individuals) / len(individuals)
        print(f'Average fitness: {average_fitness}')
