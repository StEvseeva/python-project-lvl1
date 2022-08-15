import prompt


def run_game(game):

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    print(game.DESCRIPTION)

    for correct_answers in range(3):
        question, right_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')

        if answer != right_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{right_answer}'.\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
