from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    a = randint(1, 100)
    b = randint(1, 100)
    question = str(a) + ' ' + str(b)
    answer = str(gcd(a, b))
    return question, answer
