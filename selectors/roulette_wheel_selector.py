"""Module containing roulette wheel selector"""
import random
from .selector import Selector


class RouletteWheelSelector(Selector):
    """Roulette Wheel selector class"""

    def select(self, individuals, not_same_as=None):
        """Return a selected individual from a sorted list of individuals
        that is not the same as not_same_as individual

        :param individuals: group of individuals, sorted by fitness
                            in descending order, to select from
        :param not_same_as: selected individual should not be the same as this individual
        """
        choose_from = [individual for individual in individuals if individual != not_same_as]

        base_fitness = min(choose_from).fitness
        fitnes_sum = sum(individual.fitness - base_fitness for individual in choose_from)
        relative_fitnesses = [(i.fitness - base_fitness)/fitnes_sum for i in choose_from]

        return choose_from[self.spin(relative_fitnesses)]


    @staticmethod
    def spin(weights):
        """Return chosen index based on list of weights.

        :param weights: List of weights. Sum should be 1
        """
        choice = random.random()
        choice_index = 0

        for i, weight in enumerate(weights):
            choice -= weight
            if choice < 0:
                choice_index = i
                break

        return choice_index
