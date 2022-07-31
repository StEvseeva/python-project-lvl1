from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def get_question_and_answer():
    number = randint(1, 100)
    if number % 2 == 0:
        is_number_even = 'yes'
    else:
        is_number_even = 'no'
    return str(number), is_number_even
