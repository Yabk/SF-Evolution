"""Module containing deny reinforcer"""
from .reinforcer import Reinforcer


class DenyReinforcer(Reinforcer):
    """Deny reinforcer. Gives 100 points for each deny"""

    def __init__(self):
        self.denies = 0

    def update(self, features, action):
        self.denies = features[17]

    def end(self, data):
        result = self.denies * 100
        self.denies = 0
        return result
