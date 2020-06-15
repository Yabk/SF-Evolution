"""Module containing Reporter implementation that reports iteration number on stdout"""
from .reporter import Reporter


class IterationReporter(Reporter):
    """Iteration Reporter class"""

    def __init__(self, start_at=0):
        """Initialize the reporter

        :param start_at: Starting iteration
        """
        super().__init__()
        self.current = start_at

    def report(self, individuals):
        """Report the current iteration"""
        print(f'Iteration: {self.current}')
        self.current += 1
