"""
Calculator library containing basic math operations.
"""
# My Calculator


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def divide(first_term, second_term):
    return first_term // second_term


def divide_fl(first_term, second_term):
    return first_term / second_term


def square(first_term):
    return first_term ** 2


def cube(first_term):
    return first_term ** 3


def power(first_term, second_term):
    return first_term ** second_term


def mod(first_term, second_term):
    return first_term % second_term
    # This is the modulo function that barry asked for


def square_root(first_term):
    return first_term ** (1.0 / 2)


def itob(first_term):
    """convert an int to bin"""
    if type(first_term) == int:
        return bin(first_term)
    else:
        raise TypeError
