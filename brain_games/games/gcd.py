from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    two_numbers = str(first_number) + ' ' + str(second_number)
    gsd_for_numbers = str(gcd(first_number, second_number))
    return two_numbers, gsd_for_numbers
