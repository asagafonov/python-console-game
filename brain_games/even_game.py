from random import randint
import prompt

def is_even(n):
    return True if n % 2 == 0 else False

def brain_even(rounds=3):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for round in range(rounds):
        num = randint(1, 100)
        print('Question: {}'.format(str(num)))
        user_answer = prompt.string('Your answer: ')
        if is_even(num):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        is_correct = user_answer == correct_answer
        
        if is_correct:
            print('Correct!')
        else:
            print('Let\'s try again')
            return
    print('Congratulations! You win!')
