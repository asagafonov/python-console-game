from brain_games import cli
from random import randint


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    return True if n % 2 == 0 else False


def brain_even():
    num = randint(1, 100)
    equation = '{}'.format(num)
    correct_answer = 'yes' if is_even(num) else 'no'
    return (equation, correct_answer)


def launch_game():
    cli.run_app(cli.number_of_rounds, description, brain_even)
