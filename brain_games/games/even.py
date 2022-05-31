from random import randint


def start():
    number = randint(1, 100)
    if number % 2 == 0:
        is_number_even = 'yes'
    else:
        is_number_even = 'no'
    return str(number), is_number_even
