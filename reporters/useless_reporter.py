"""Module containing the useless Reporter implementation"""
from .reporter import Reporter


class UselessReporter(Reporter):
    """Useless Reporter that does nothing"""

    def report(self, individuals):
        """Do nothing"""
