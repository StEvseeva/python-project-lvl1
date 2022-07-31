import prompt


def run_game(game):

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print('Hello, %s!' % name)

    print(game.DESCRIPTION)

    correct_answers = 0
    right_answer = ''
    while correct_answers < 3:
        question, right_answer = game.get_question_and_answer()
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
