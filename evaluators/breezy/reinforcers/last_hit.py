"""Module containing last hit reinforcer"""
from .reinforcer import Reinforcer


class LastHitReinforcer(Reinforcer):
    """Last hit reinforcer. Gives 100 points for each last hit"""

    def __init__(self):
        self.last_hits = 0

    def update(self, features, action):
        self.last_hits = features[16]

    def end(self, data):
        result = self.last_hits * 100
        self.last_hits = 0
        return result
