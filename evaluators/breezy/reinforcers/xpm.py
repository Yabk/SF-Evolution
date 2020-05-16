"""Module containing XPM reinforcer"""
from .reinforcer import Reinforcer


class XPMReinforcer(Reinforcer):
    """XPM reinforcer. Gives XPM amount as points"""

    XP_AMOUNTS = [0, 115.0, 415.0, 840.0, 1370.0, 1960.0, 2620.0, 3355.0, 4175.0, 5085.0, 6035.0,
                  7025.0, 8055.0, 9192.5, 10430.0, 11692.5, 12980.0, 14292.5, 15705.0, 17250.0,
                  18845.0, 20570.0, 22545.0, 24770.0, 27245.0, 30295.0, 34295.0, 39295.0, 45295.0,
                  52295.0, 56045]

    def __init__(self, multiplier=1):
        self.level = 1
        self.time = 0
        self.multiplier = multiplier

    def update(self, features, action):
        self.level = features[0]
        self.time = features[39]

    def end(self, data):
        return self.XP_AMOUNTS[self.level] * 60/self.time * self.multiplier
