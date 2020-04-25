"""Module containing Evolution strategy algorithm implementation"""
import random
from .algorithm import Algorithm


class EvolutionStrategy(Algorithm):
    """Evolution strategy class"""

    def __init__(self, reporters, max_iterations, evaluator, individual_generator,
                 parent_count, children_count, mutation,
                 elitism=False, crossover=None, target_fitness=None):
        """Initialize hyperparamters of the algorithm.

        :param reporters: List of Reporter instances
        :param max_iterations: Max iterations of the algorithm
        :param evaluator: Evaluator instance
        :param individual_generator: Individual factory
        :param parent_count: mu - size of the parent population
        :param children_count: lambda - size of offspring created in each iteration
        :param mutation: Mutation to be used
        :param elitism: If true, uses both parent and offspring population for selection.
        :param crossover: Crossover to be used. If None, only mutation is used.
        :param target_fitness: If an individual reaches target_fitness the algorithm is stopped.
                               If None, algorithm won't be stopped based on fitness.
        """
        super().__init__(reporters, max_iterations, evaluator, individual_generator, target_fitness)
        self.parent_count = parent_count
        self.children_count = children_count
        self.mutation = mutation
        self.elitism = elitism
        self.crossover = crossover

        self.population = individual_generator.batch_generate(self.parent_count)
        self.children_population = None


    def run(self):
        """Run the algorithm"""

        self.evaluator.batch_evaluate(self.population)
        self._report()
        self.best_individual = self.population[0]
        if self._stop_condition():
            self._save_best_individual()
            return

        self.iteration = 1
        while self.iteration != self.max_iterations:
            self.children_population = []

            # Reproduction
            if self.crossover is not None:
                self._cross_parents()
            else:
                parents = random.choices(self.population, k=self.children_count)
                self.children_population = [parent.copy() for parent in parents]

            self.mutation.batch_mutate(self.children_population)

            # Evalutation
            self.evaluator.batch_evaluate(self.children_population)

            # Generation change
            if not self.elitism:
                self.population = self.children_population[:self.parent_count]
            else:
                self.population = sorted(self.children_population+self.population,
                                         key=lambda individual: individual.fitness,
                                         reverse=True)[:self.parent_count]

            self._report()
            if self._check_iteration():
                break

        self._save_best_individual()


    def _cross_parents(self):
        """Cross parents until children_population is full"""
        while len(self.children_population) < self.children_count:
            parent_1, parent_2 = random.sample(self.population, k=2)
            self.children_population.extend(self.crossover.cross(parent_1, parent_2))
