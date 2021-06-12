from random import randint
import prompt

operations = ['+', '-', '*']

def is_even(n):
    return True if n % 2 == 0 else False

def brain_calc(rounds=3):
    print('What is the result of the expression?')
    for round in range(rounds):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        random_operation_index = randint(0, 2)
        print('Question: {} {} {}'.format(str(num1), operations[random_operation_index], str(num2)))
        user_answer = prompt.string('Your answer: ')

        if operations[random_operation_index] == '+':
            correct_answer = num1 + num2
            is_correct = True if int(user_answer) == correct_answer else False
        elif operations[random_operation_index] == '-':
            correct_answer = num1 - num2
            is_correct = True if int(user_answer) == correct_answer else False
        elif operations[random_operation_index] == '*':
            correct_answer = num1 * num2
            is_correct = True if int(user_answer) == correct_answer else False
        else:
            is_correct = False

        if is_correct:
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was: "{}"'.format(str(user_answer), str(correct_answer)))
            print('Let\'s try again')
            return
    print('Congratulations! You win!')
