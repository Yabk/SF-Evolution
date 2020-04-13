"""Module containing genetic algorithm implementation"""
from .algorithm import Algorithm


class GeneticAlgorithm(Algorithm):
    """Genetic algorithm class"""

    def __init__(self, evaluator, reporter, selector, crossover, mutation,
                 population_size, individual_generator, max_iterations):
        """Initialize genetic algorithm hyperparameters.

        :param evaluator: Evaluator instance
        :param reporter: Reporter instance
        :param selector: Selector to be used
        :param crossover: Crossover to be used
        :param mutation: Mutation to be used
        :param population_size: population size
        :param individual_generator: Individual factory
        :param max_iterations: Maximum iterations of the algorithm.
                               If set to less than 0, algorithm will run indefinitely.
        """
        super().__init__()
        self.evaluator = evaluator
        self.reporter = reporter
        self.selector = selector
        self.crossover = crossover
        self.mutation = mutation
        self.population_size = population_size
        self.max_iterations = max_iterations
        self.population = individual_generator.batch_generate(population_size)


    def run(self):
        """Run the genetic algorithm"""

        self.evaluator.batch_evaluate(self.population)
        self.best_individual = self.population[0]
        self.reporter.report(self.population)

        iteration = 1
        while iteration != self.max_iterations:
            print(f'Iteration : {iteration}')
            next_population = []

            while len(next_population) > self.population_size:
                parent_1 = self.selector.select(self.population)
                parent_2 = self.selector.select(self.population)
                next_population.extend(self.crossover.crossover(parent_1, parent_2))

            self.population = next_population
            self.evaluator.batch_evaluate(self.population)
            if self.population[0].fitness > self.best_individual.fitness:
                self.best_individual = self.population[0]
            self.reporter.report(self.population)
            iteration += 1

        self.save_best_individual()
