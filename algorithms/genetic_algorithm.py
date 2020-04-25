"""Module containing genetic algorithm implementation"""
from .algorithm import Algorithm


class GeneticAlgorithm(Algorithm):
    """Genetic algorithm class"""

    def __init__(self, reporters, evaluator, selector, crossover, mutation,
                 population_size, individual_generator, max_iterations, target_fitness=None):
        """Initialize genetic algorithm hyperparameters.

        :param evaluator: Evaluator instance
        :param reporters: List of Reporter instances
        :param selector: Selector to be used
        :param crossover: Crossover to be used
        :param mutation: Mutation to be used
        :param population_size: population size
        :param individual_generator: Individual factory
        :param max_iterations: Maximum iterations of the algorithm.
                               If set to 0 or less, algorithm will run indefinitely.
        """
        super().__init__(reporters, max_iterations, evaluator, individual_generator, target_fitness)
        self.selector = selector
        self.crossover = crossover
        self.mutation = mutation
        self.population_size = population_size
        self.population = individual_generator.batch_generate(population_size)


    def run(self):
        """Run the genetic algorithm"""

        self.evaluator.batch_evaluate(self.population)
        self._report()

        self.best_individual = self.population[0]
        if self._stop_condition():
            self._save_best_individual()
            return


        self.iteration = 1
        while self.iteration != self.max_iterations:
            next_population = []

            while len(next_population) < self.population_size:
                parent_1 = self.selector.select(self.population)
                parent_2 = self.selector.select(self.population)
                children = self.crossover.cross(parent_1, parent_2)
                self.mutation.batch_mutate(children)
                next_population.extend(children)

            self.population = next_population
            self.evaluator.batch_evaluate(self.population)
            self._report()

            if self._check_iteration():
                break

        self._save_best_individual()
