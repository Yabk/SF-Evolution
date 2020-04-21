"""Module containing simple CGP mutation"""
import random
from ..mutation import Mutation


class CGPMutation(Mutation):
    """Simple mutation for CGPIndividual"""

    def __init__(self, n=1):
        """Initialize the mutation

        :param n: Number of mutations to perform
        """
        super().__init__()
        self.n = n


    def mutate(self, individual):
        """
        Mutates the given individual.

        :param individual: the individual to mutate
        """
        indices = random.sample(range(len(individual.chromosome)), k=self.n)
        for index in indices:
            self.mutate_index(individual, index)


    @staticmethod
    def mutate_index(individual, index):
        """Mutate a CGP individual on given index."""

        node_count = individual.grid_width * individual.grid_height
        if index >= node_count*3 + individual.constant_len:
            # Index defines one of individual's outputs
            individual.chromosome[index] = random.randrange(individual.input_len +
                                                            individual.constant_len + node_count)

        elif index < individual.constant_len:
            # Index defines one of individual's constants
            individual.chromosome[index] = random.randrange(len(individual.constants))

        else:
            if (index - individual.constant_len + 1) % 3 == 0:
                # Index defines module function
                individual.chromosome[index] = random.randrange(len(individual.modules))
            else:
                # Index defines module input
                module_index = (index - individual.constant_len) // 3
                layer_index = module_index // individual.grid_height

                valid_input_len = (individual.input_len + individual.constant_len
                                   + individual.grid_height * layer_index)
                individual.chromosome[index] = random.randrange(valid_input_len)
