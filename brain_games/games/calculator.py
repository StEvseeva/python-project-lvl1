from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'

def get_question_and_answer():
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
