from brain_games import cli
from math import gcd
from random import randint


description = 'What is the greatest common divisor?'


def brain_gcd():
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    equation = '{} {}'.format(num1, num2)
    correct_answer = gcd(num1, num2)

    return (equation, correct_answer)


def launch_game():
    cli.run_app(cli.number_of_rounds, description, brain_gcd)
