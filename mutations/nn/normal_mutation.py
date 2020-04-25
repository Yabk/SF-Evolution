"""Module containing normal mutation for NNIndividual"""
import numpy as np
from ..mutation import Mutation


class NNNormalMutation(Mutation):
    """Mutation adds a random value from normal distribution to each weight"""

    def __init__(self, stddev=0.01):
        """Initilize the mutation

        :param stddev: Standard deviation for random values from normal distribution
        """
        super().__init__()
        self.stddev = stddev

    def mutate(self, individual):
        """Mutate given Neural Network Individual"""
        for layer in individual.chromosome:
            layer.weights += np.random.normal(scale=self.stddev, size=layer.weights.shape)
            layer.biases += np.random.normal(scale=self.stddev, size=layer.biases.shape)
