from algorithms.evolution_strategy import EvolutionStrategy
from reporters.best_individual_reporter import BestIndividualReporter
from evaluators.breezy.breezy import BreezyEvaluator
from evaluators.breezy.reinforcers import last_hit, win
from mutations.cgp.smart_mutation import CGPSmartMutation
from genotypes.cgp.cgp import CGPIndividual
from genotypes.individual import IndividualGenerator

def main():
    evaluator = BreezyEvaluator((last_hit.LastHitReinforcer(), win.WinReinforcer()),
                                listener_address=('192.168.88.152', 8088),
                                breezy_url='http://192.168.88.26:8085')

    reporters = [BestIndividualReporter()]

    cgp_hyperparams = {
        'input_len': evaluator.input_len,
        'grid_size': (50, 30),
        'output_len': evaluator.output_len,
        'constant_len': 4
    }
    generator = IndividualGenerator(CGPIndividual, cgp_hyperparams)

    mutation = CGPSmartMutation(n=4)

    max_iterations = 0
    parent_count = 2
    children_count = 4
    alg = EvolutionStrategy(reporters, max_iterations, evaluator, generator,
                            parent_count, children_count, mutation, elitism=True, target_fitness=1000000)

    alg.run()

if __name__ == "__main__":
    main()
