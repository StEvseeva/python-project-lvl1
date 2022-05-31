from random import randint, choice


def start():
    a = randint(0, 100)
    b = randint(0, 100)
    sign = choice(['+', '-', '*'])
    expression = str(a) + ' ' + sign + ' ' + str(b)
    if sign == '+':
        answer = str(a + b)
    elif sign == '-':
        answer = str(a - b)
    else:
        answer = str(a * b)
    return expression, answer
