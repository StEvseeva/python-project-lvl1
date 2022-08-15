from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = randint(1, 100)
    answer = 'yes' if is_prime(number) else 'no'
    return str(number), answer


def is_prime(number):
    for divider in range(2, (number // 2) + 1):
        if number % divider == 0:
            return False
    return True