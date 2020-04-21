"""CGP modules"""
import math


PROTECTED_DIVISION_EPSILON = 1e-5


def module_sum(a, b):
    """Module function - sum"""
    return a + b


def module_difference(a, b):
    """Module function - difference"""
    return a - b


def module_product(a, b):
    """Module function - product"""
    return a * b


def module_quotient(a, b):
    """Module function - quotient"""
    return a / b if abs(b) > PROTECTED_DIVISION_EPSILON else a


def module_sine(a, b):
    """Module function - sine"""
    return math.sin(a)


def module_cosine(a, b):
    """Module function - cosine"""
    return math.cos(a)


def module_negative(a, b):
    """Module function - negative first argument"""
    return -a
