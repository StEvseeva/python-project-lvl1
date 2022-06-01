from random import randint


def start():
    count = randint(5, 10)
    step = randint(1, 20)
    number = randint(1, 50)
    end = number + count * step
    empty_place = number + randint(0, count) * step
    progression = ''
    answer = 'place' + str(empty_place)
    for number in range(number, end + step, step):
        if number != empty_place:
            progression += (str(number) + ' ')
        else:
            progression += '.. '
            answer = str(number)
    return progression, answer
