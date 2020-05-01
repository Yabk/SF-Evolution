"""Module containing k-point crossover"""
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
            raise ValueError(f'Number of crossover points must be greater than 0. {k} was given')
        self.k = k


    def cross(self, parent_1, parent_2):
        """Return 2 children made by k-point crossover between the parents.
        Parents should have their chromosomes as lists in attribute named chromosome.
        Cromosomes should be of equal length.
        """
        child_chromosomes = self._cross_chromosomes(parent_1.chromosome, parent_2.chromosome)

        child_1 = self.individual_generator.generate(child_chromosomes[0])
        child_2 = self.individual_generator.generate(child_chromosomes[1])

        return child_1, child_2


    def _cross_chromosomes(self, parent_chromo_1, parent_chromo_2):
        """Cross 2 given chromosomes that are represented as one dimensional lists"""
        points = sorted(random.sample(range(1, len(parent_chromo_1)), self.k))
        chromosome_1 = []
        chromosome_2 = []

        switch = False
        prev_point = 0
        for point in points:
            if switch:
                chromosome_1 += parent_chromo_2[prev_point:point]
                chromosome_2 += parent_chromo_1[prev_point:point]
            else:
                chromosome_1 += parent_chromo_1[prev_point:point]
                chromosome_2 += parent_chromo_2[prev_point:point]
            prev_point = point
            switch = not switch

        if switch:
            chromosome_1 += parent_chromo_2[prev_point:]
            chromosome_2 += parent_chromo_1[prev_point:]
        else:
            chromosome_1 += parent_chromo_1[prev_point:]
            chromosome_2 += parent_chromo_2[prev_point:]

        return chromosome_1, chromosome_2
