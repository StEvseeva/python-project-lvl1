from random import randint
from math import gcd


def start():
    a = randint(1, 100)
    b = randint(1, 100)
    question = str(a) + ' ' + ' ' + str(b)
    answer = str(gcd(a, b))
    return question, answer
