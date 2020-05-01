"""Module containing k-point crossover for NNIndividual"""
from genotypes.nn.nn import NNIndividual
from .point_crossover import PointCrossover


class NNPointCrossover(PointCrossover):
    """k-point crossover for NNIndividual"""

    def cross(self, parent_1, parent_2):
        """Return 2 children made by k-point crossover between the parents"""
        child_chromosomes = self._cross_chromosomes(parent_1.serialize(), parent_2.serialize())
        layers = self.individual_generator.layers
        activation_functions = self.individual_generator.activation_functions

        child_1 = NNIndividual.deserialize(child_chromosomes[0], layers, activation_functions)
        child_2 = NNIndividual.deserialize(child_chromosomes[1], layers, activation_functions)

        return child_1, child_2
