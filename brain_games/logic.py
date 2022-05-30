from random import randint
import prompt


def construct():
    name = welcome()
    game(name)


def welcome():
    name = prompt.string('May I have your name? ')
    print('Hello, %s!' % name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def game(name):
    correct_answers = 0
    while correct_answers < 3:
        number = randint(1, 100)
        if number % 2 == 0:
            is_number_even = 'yes'
        else:
            is_number_even = 'no'
        print('Question: %d' % number)
        answer = prompt.string('Your answer: ')
        if answer == is_number_even:
            correct_answers += 1
            print('Correct!')
        else:
            print("'%s' is wrong answer ;(. Correct answer was"
                  " '%s'.\nLet's try again, %s!" % (answer,
                                                    is_number_even,
                                                    name))
            return
    print('Congratulations, %s!' % (name))
