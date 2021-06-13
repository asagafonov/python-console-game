import prompt


number_of_rounds = 3


def run_app(rounds, description, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    print(description)
    for round in range(rounds):
        new_game = game()
        (equation, correct_answer) = new_game
        print('Question: {}'.format(equation))
        user_answer = prompt.string('Your answer: ')
        is_correct = user_answer == str(correct_answer)
        if is_correct:
            print('Correct!')
        else:
            template = '"{}" is wrong answer ;(. Correct answer was: "{}"'
            print(template.format(user_answer, correct_answer))
            print('Let\'s try again, {}'.format(name))
            return
    print('Congratulations, {}! You win!'.format(name))
