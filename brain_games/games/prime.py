from random import randint


def start():
    number = randint(1, 100)
    answer = 'yes'
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            answer = 'no'
            break
    return str(number), answer
