"""Module containing k-point point crossover"""
import random
from .crossover import Crossover


class PointCrossover(Crossover):
    """k-point crossover class"""

    def __init__(self, individual_generator, k):
        """Initialize the crossover

        :param individual_generator: Generator that will be used to generate children
        :param k: Number of crossover points
        """
        super().__init__(individual_generator)

        if k < 1:
            raise ValueError(f'Number of crossover points must be greater than 1. {k} was given')
        self.k = k


    def cross(self, parent_1, parent_2):
        """Return 2 children made by k-point crossover between the parents.
        Parents should have their chromosomes as lists in attribute named chromosome.
        Cromosomes should be of equal length.
        """
        points = sorted(random.sample(range(1, len(parent_1.chromosome)), self.k))
        chromosome_1 = []
        chromosome_2 = []

        switch = False
        prev_point = 0
        for point in points:
            if switch:
                chromosome_1 += parent_2.chromosome[prev_point:point]
                chromosome_2 += parent_1.chromosome[prev_point:point]
            else:
                chromosome_1 += parent_1.chromosome[prev_point:point]
                chromosome_2 += parent_2.chromosome[prev_point:point]
            prev_point = point
            switch = not switch

        if switch:
            chromosome_1 += parent_2.chromosome[prev_point:]
            chromosome_2 += parent_1.chromosome[prev_point:]
        else:
            chromosome_1 += parent_1.chromosome[prev_point:]
            chromosome_2 += parent_2.chromosome[prev_point:]

        child_1 = self.individual_generator.generate(chromosome_1)
        child_2 = self.individual_generator.generate(chromosome_2)

        return child_1, child_2
