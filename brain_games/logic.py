from brain_games.games.even import start as even_start
from brain_games.games.calculator import start as calculator_start
from brain_games.games.gcd import start as gcd_start
from brain_games.games.progression import start as progression_start
from brain_games.games.prime import start as prime_start
import prompt


def construct(game_name):
    name = welcome(game_name)
    game(game_name, name)


def welcome(game_name):
    name = prompt.string('May I have your name? ')
    print('Hello, %s!' % name)
    if game_name == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game_name == 'calculator':
        print('What is the result of the expression?')
    elif game_name == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game_name == 'progression':
        print('What number is missing in the progression?')
    else:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return name


def game(game_name, name):
    correct_answers = 0
    right_answer = ''
    while correct_answers < 3:
        question = ''
        if game_name == 'even':
            question, right_answer = even_start()
        elif game_name == 'calculator':
            question, right_answer = calculator_start()
        elif game_name == 'gcd':
            question, right_answer = gcd_start()
        elif game_name == 'progression':
            question, right_answer = progression_start()
        else:
            question, right_answer = prime_start()
        print('Question: %s' % question)
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            correct_answers += 1
            print('Correct!')
        else:
            print("'%s' is wrong answer ;(. Correct answer was"
                  " '%s'.\nLet's try again, %s!" % (answer,
                                                    right_answer,
                                                    name))
            return
    print('Congratulations, %s!' % (name))
