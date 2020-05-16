"""Module containing last hit reinforcer"""
from .reinforcer import Reinforcer


class LastHitReinforcer(Reinforcer):
    """Last hit reinforcer. Gives points equal to the number of denies times the multiplier"""

    def __init__(self, multiplier=100):
        self.last_hits = 0
        self.multiplier = multiplier

    def update(self, features, action):
        self.last_hits = features[16]

    def end(self, data):
        result = self.last_hits * self.multiplier
        self.last_hits = 0
        return result
