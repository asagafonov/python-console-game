from math import sqrt
from random import randint
from itertools import count, islice
import prompt

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def brain_prime(rounds=3):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for round in range(rounds):
        num = randint(1, 100)
        print('Question: {}'.format(str(num)))
        user_answer = prompt.string('Your answer: ')
        if is_prime(num):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        is_correct = correct_answer == user_answer

        if is_correct:
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was: "{}"'.format(user_answer, correct_answer))
            print('Let\'s try again')
            return
    print('Congratulations! You win!')
