from math import gcd
from random import randint
import prompt

def brain_gcd(rounds=3):
    print('Find the greatest common divisor of given numbers.')
    for round in range(rounds):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        print('Question: {} {}'.format(str(num1), str(num2)))
        correct_answer = gcd(num1, num2)
        user_answer = prompt.string('Your answer: ')

        is_correct = int(user_answer) == correct_answer

        if is_correct:
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was: "{}"'.format(str(user_answer), str(correct_answer)))
            print('Let\'s try again')
            return
    print('Congratulations! You win!')
