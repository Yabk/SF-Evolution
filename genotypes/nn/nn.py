"""Module containing Neural Network model of an Individual"""
import codecs
import pickle
from copy import deepcopy
import numpy as np
from ..individual import Individual, IndividualGenerator


class NNGenerator(IndividualGenerator):
    """A Neural Network factory"""

    def __init__(self, layers, activation_functions):
        """Initialize the neural network hyperparameters

        :param layers: Layer architecture. A list of neuron counts for each layer.
        :param activation_functions: A list of activation_functions for each layer.
        """
        super().__init__()
        self.layers = layers
        self.activation_functions = activation_functions

    def generate(self, chromosome=None):
        """Generate an individual using predefined hyperparameters.

        :param chromosome: Use given chromosome value for new individual
                           Random if None
        """
        return NNIndividual(self.layers, self.activation_functions, chromosome=chromosome)


class NNIndividual(Individual):
    """A Neural Network Individual"""

    def __init__(self, layers, activation_functions, chromosome=None):
        """Initialize NNIndividual.

        :param layers: Layer architecture.
                       A list of neuron counts for each layer as well as input count for first layer
        :param activation_functions: A list of activation_functions for each layer.
        :param chromosome: A list of NNLayers. Individual is randomized if None.
        """
        super().__init__()
        if chromosome:
            self.chromosome = deepcopy(chromosome)
        else:
            self.chromosome = []
            for i, activation in enumerate(activation_functions):
                self.chromosome.append(NNLayer(layers[i], layers[i+1], activation))


    def evaluate(self, inputs):
        """Evaluate given inputs and return outputs"""
        result = np.array([inputs]).swapaxes(0, 1)
        for layer in self.chromosome:
            result = layer.propagate(result)
        return list(result.swapaxes(0, 1)[0])


    def to_file(self, file_path):
        """Save the individual to a file"""
        with open(file_path, 'w') as export_file:
            for layer in self.chromosome:
                export_file.write(str(layer)+'\n')
            export_file.write(str(self.fitness))


    @staticmethod
    def from_file(file_path):
        """Import NNIndividual from a text file"""
        with open(file_path, 'r') as import_file:
            lines = import_file.readlines()

        chromosome = []
        while '\n' in lines:
            chromosome.append(NNLayer.from_string(''.join(lines[:lines.index('\n')])))
            lines = lines[lines.index('\n')+1:]
        fitness = float(lines[0])

        nn = NNIndividual(0, 0, chromosome=chromosome)
        nn.fitness = fitness

        return nn


class NNLayer:
    """A Neural Network layer"""

    def __init__(self, input_count, neuron_count, activation_function):
        self.activation_function = activation_function
        self.weights = np.random.randn(neuron_count, input_count) * 0.1
        self.biases = np.random.randn(neuron_count, 1) * 0.1

    def propagate(self, values):
        """Propagate given values throught the layer"""
        return self.activation_function(np.dot(self.weights, values) + self.biases)

    def __str__(self):
        """Pickle the layer and save it to string"""
        return codecs.encode(pickle.dumps(self), 'base64').decode()

    @staticmethod
    def from_string(string):
        """Load a NNLayer from a string"""
        return pickle.loads(codecs.decode(string.encode(), 'base64'))
