from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    number = randint(1, 100)
    is_number_even = 'yes' if number % 2 == 0 else 'no'
    return str(number), is_number_even
