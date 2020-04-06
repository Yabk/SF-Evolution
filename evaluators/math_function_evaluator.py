"""Module containing Evaluator for custom math function"""
from py_expression_eval import Parser
from .evaluator import Evaluator


class MathFunctionEvaluator(Evaluator):
    """Math function evaluator class"""

    def __init__(self, expression, sample_points):
        """Initialize the Evaluator
        :param expression: string of a math expression
        :param sample_points: list of sample points (tuples)
        """
        expression = Parser().parse(expression)
        variables = expression.variables()
        super().__init__(len(variables), 1)
        self.inputs = sample_points
        inputs_dicts = [dict(zip(variables, sample_point)) for sample_point in sample_points]
        self.outputs = [expression.evaluate(input_dict) for input_dict in inputs_dicts]

    def evaluate(self, individual):
        """Evaluate the individual across all sample points using MSE.
        Fitness is calculated as a negative MSE
        """
        outputs = [individual.evaluate(point)[0] for point in self.inputs]
        diffs = [(output - expected)**2 for output, expected in zip(outputs, self.outputs)]
        individual.fitness = - sum(diffs) / len(diffs)
