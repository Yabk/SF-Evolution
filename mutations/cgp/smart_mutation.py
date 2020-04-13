"""Module containing Smart CGP Mutation"""
import random
from .simple_mutation import CGPMutation


class CGPSmartMutation(CGPMutation):
    """Mutation for CGPIndividual that mutates only active modules"""


    def mutate(self, individual):
        """
        Mutates the given individual.

        :param individual: the individual to mutate
        """
        active_indices = self._get_active_indices(individual)
        indices = random.sample(active_indices, k=self.n)
        for index in indices:
            self.mutate_index(individual, index)


    @staticmethod
    def _get_active_indices(individual):
        """Return a list of active indices for given individual"""
        active_modules = set()
        active_indices = set()
        to_check = set()

        for i in range(len(individual.chromosome)-individual.output_len,
                       len(individual.chromosome)):
            active_indices.add(i)

        for output in individual.chromosome[-individual.output_len:]:
            if output >= individual.input_len:
                to_check.add(output)

        while to_check:
            current = to_check.pop()
            active_modules.add(current)
            index = individual.module_index(current)
            if ((individual.chromosome[index + 0] >= individual.input_len) and
                    individual.chromosome[index + 0] not in active_modules):
                to_check.add(individual.chromosome[index + 0])
            if ((individual.chromosome[index + 1] >= individual.input_len) and
                    individual.chromosome[index + 1] not in active_modules):
                to_check.add(individual.chromosome[index + 1])
            active_indices.add(index + 0)
            active_indices.add(index + 1)
            active_indices.add(index + 2)

        return list(active_indices)
