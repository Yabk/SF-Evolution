"""Module containing deny reinforcer"""
from .reinforcer import Reinforcer


class DenyReinforcer(Reinforcer):
    """Deny reinforcer. Gives points equal to the number of denies times the multiplier"""

    def __init__(self, multiplier=100):
        self.denies = 0
        self.multiplier = multiplier

    def update(self, features, action):
        self.denies = features[17]

    def end(self, data):
        result = self.denies * self.multiplier
        self.denies = 0
        return result
