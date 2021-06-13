from brain_games import cli
from math import sqrt
from random import randint
from itertools import count, islice


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def brain_prime():
    num = randint(1, 100)
    equation = '{}'.format(num)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return (equation, correct_answer)


def launch_game():
    cli.run_app(cli.number_of_rounds, description, brain_prime)
