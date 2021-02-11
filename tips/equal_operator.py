"""
compare efficiency between the statement 'is' and '=='
reference: [link](https://medium.com/swlh/is-and-in-python-f084f36cbc0e)
"""
import sys
import time


def time_calculator(function):
    def wrap(*args, **kwargs):
        start = time.time()
        output = function(*args, **kwargs)
        end = time.time()
        print('{} cost {} seconds'.format(function.__name__, end-start))
        return output
    return wrap


@time_calculator
def equality_operator(n):
    a = 'Which one is best? identity or equality ?' * 1000
    b = 'Which one is best? identity or equality ?' * 1000
    for i in range(n):
        if a == b:
            pass


@time_calculator
def identity_operator(n):
    a = 'Which one is best? identity or equality ?' * 1000
    b = 'Which one is best? identity or equality ?' * 1000
    for i in range(n):
        if a is b:
            pass


if __name__ == '__main__':
    equality_operator(10000000)
    identity_operator(10000000)