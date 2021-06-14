from brain_games import cli
from random import randint


description = 'What number is missing in the progression?'


def generate_progression(step, length):
    progression = []
    progression_start = randint(1, 100)
    el = progression_start
    for i in range(length):
        progression.append(str(el))
        el += step
    return progression


def brain_progression():
    progression_length = 10
    progression_step = randint(1, 10)
    progression = generate_progression(progression_step, progression_length)
    hidden_el_index = randint(0, progression_length - 1)
    hidden_progression = progression[:]
    hidden_progression[hidden_el_index] = '..'

    equation = ' '.join(hidden_progression)
    correct_answer = progression[hidden_el_index]

    return (equation, correct_answer)


def launch_game():
    cli.run_app(cli.number_of_rounds, description, brain_progression)
