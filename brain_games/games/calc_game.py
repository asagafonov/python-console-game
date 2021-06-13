from brain_games import cli
from random import randint


description = 'What is the result of the expression?'


operations = ['+', '-', '*']


def is_even(n):
    return True if n % 2 == 0 else False


def brain_calc():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    random_operation_index = randint(0, len(operations) - 1)

    if operations[random_operation_index] == '+':
        equation = '{} + {}'.format(num1, num2)
        correct_answer = num1 + num2
    elif operations[random_operation_index] == '-':
        equation = '{} - {}'.format(num1, num2)
        correct_answer = num1 - num2
    elif operations[random_operation_index] == '*':
        equation = '{} * {}'.format(num1, num2)
        correct_answer = num1 * num2

    return (equation, correct_answer)


def launch_game():
    cli.run_app(cli.number_of_rounds, description, brain_calc)
