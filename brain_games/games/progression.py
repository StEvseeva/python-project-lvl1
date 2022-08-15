from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    length = randint(5, 10)
    step = randint(1, 20)
    start = randint(1, 50)
    end = start + length * step
    empty_place = start + randint(0, length) * step
    progression = list(map(str, range(start, end+1, step)))
    missing_number, progression[empty_place] = progression[empty_place], '..'
    progression = ' '.join(progression)
    return progression, missing_number
