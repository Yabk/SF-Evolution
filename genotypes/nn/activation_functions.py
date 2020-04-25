"""Activation functions for Neural Network Individuals"""
import numpy as np


def sigmoid(values):
    """Sigmoid activation function"""
    return 1/(1+np.exp(-values))


def relu(values):
    """Rectified Lineaar Unit activation function"""
    return np.maximum(0, values)
