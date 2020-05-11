"""Module containing win reinforcer"""
from .reinforcer import Reinforcer


class WinReinforcer(Reinforcer):
    """Win reinforcer. Gives 1 000 000 points for winning the game"""

    def update(self, features, action):
        pass

    def end(self, data):
        if data['winner'] == 'Dire':
            return 0
        return 1000000
