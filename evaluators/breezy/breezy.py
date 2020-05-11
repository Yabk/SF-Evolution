"""Module containing evaluator for breezy server"""
import math
import copy
import requests
from ..evaluator import Evaluator
from .listener import Listener


class BreezyEvaluator(Evaluator):
    """Breezy Evaluator class"""

    # indices of features that are going to be used unprocessed
    RAW_FEATURES = (1, 3, 4, 5, 6, 7, 8, 11, 12, 14, 15, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29,
                    31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 44, 45, 49, 50, 51, 52, 53, 56, 58,
                    59, 64, 65, 225, 226, 229, 236, 243, 246, 253, 260, 261, 264, 267, 268, 271,
                    278, 285, 288, 295, 302, 303, 306, 309)
    CREEPS_INDICES = range(85, 211, 14)

    def __init__(self, reinforcers, listener_address=('127.0.0.1', 8086),
                 breezy_url='http://127.0.0.1:8085'):
        """Initialize the Evaluator

        :param listener_address: (string, int) tuple containing ip address and
                                 port that the listener will use
        :param breezy_url: Url to breezy server
        :param reinforcers: List of reinforcers
        """
        super().__init__(111, 26)
        self.listener = Listener(self, address=listener_address, breezy_url=breezy_url)
        self.breezy_url = breezy_url
        self.reinforcers = reinforcers
        self.individuals = []


    def callback(self, features):
        """Callback method for listener

        :param features: List of features received from breezy server
        """
        processed = self._process(features)
        actions = self.individuals[0].evaluate(processed)
        action = actions.index(max(actions))
        action = action if action < 9 else action+4
        for reinforcer in self.reinforcers:
            reinforcer.update(processed, action)
        return action


    def game_done(self, data):
        """Callback method for finished runs

        :param data: Data received from breezy server
        """
        fitness = 0
        for reinforcer in self.reinforcers:
            fitness += reinforcer.end(data)
        self.individuals.pop(0).fitness = fitness

        if 'webhook' in data:
            webhook_url = self.breezy_url+data['webhook']
            requests.get(url=webhook_url)


    def evaluate(self, individual):
        self.batch_evaluate([individual])


    def batch_evaluate(self, individuals):
        self.individuals = copy.copy(individuals)
        self.listener.start(len(individuals))
        self.listener.join()


    @staticmethod
    def _process(data):
        processed = [data[i] for i in BreezyEvaluator.RAW_FEATURES]

        time_since_last_attack = data[56] - (data[17] - 63.1) # index 65
        time_since_last_attack_opp = data[56] - (data[47] - 63.1)
        health_normalized = data[2]/data[3]
        health_opp_normalized = data[32]/data[33]
        mana_normalized = data[5]/data[6]
        mana_opp_normalized = data[35]/data[36]
        tower_health_normalized = data[58]/data[59]
        tower_opp_health_normalized = data[64]/data[65]
        processed.extend((time_since_last_attack, time_since_last_attack_opp,
                          health_normalized, health_opp_normalized,
                          mana_normalized, mana_opp_normalized,
                          tower_health_normalized, tower_opp_health_normalized))

        # Process creep features
        pos_1_sum = 0
        pos_2_sum = 0
        creep_count = 0
        for i in BreezyEvaluator.CREEPS_INDICES:
            if data[i+2] == -1:
                creep_type = -1 # No creep
                processed.extend((creep_type, -1, -1, -1))
            else:
                if data[i+2] == 875:
                    creep_type = 3 # Siege creep
                elif data[i+2] < 550:
                    creep_type = 1 # Ranged creep
                else:
                    creep_type = 2 # Melee creep
                creep_health_normalized = data[i+1]/data[i+2]
                creep_distance = math.sqrt((data[i+12]-data[26])**2 + (data[i+13]-data[27])**2)
                can_attack = 1 if creep_distance < 500 else -1

                processed.extend((creep_type, creep_health_normalized, creep_distance, can_attack))

                creep_count += 1
                pos_1_sum += data[i+12]
                pos_2_sum += data[i+13]

        if creep_count == 0:
            processed.extend((-1, -1))
        else:
            processed.extend((pos_1_sum/creep_count, pos_2_sum/creep_count))

        return processed
