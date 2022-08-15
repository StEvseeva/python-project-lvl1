from random import randint, choice
from operator import add, sub, mul
import random

DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    operand1 = randint(0, 100)
    operand2 = randint(0, 100)
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
    }

    operation = random.choice(list(operations.keys()))
    expression = str(operand1) + ' ' + operation + ' ' + str(operand2)
    expression_answer = str(operations[operation](operand1, operand2))

    return expression, expression_answer

