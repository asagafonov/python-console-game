from random import randint
import prompt

def generate_progression(step, length):
    progression = []
    progression_start = randint(1, 100)
    el = progression_start
    for i in range(length):
        progression.append(str(el))
        el += step
    return progression

def brain_progression(rounds=3):
    print('What number is missing in the progression?')
    for round in range(rounds):
        progression_length = 10
        progression_step = randint(1, 10)
        progression = generate_progression(progression_step, progression_length)
        hidden_el_index = randint(0, 9)
        hidden_progression = progression[:]
        hidden_progression[hidden_el_index] = '..'

        print('Question: {}'.format(' '.join(hidden_progression)))
        correct_answer = progression[hidden_el_index]
        user_answer = prompt.string('Your answer: ')

        is_correct = user_answer == correct_answer

        if is_correct:
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was: "{}"'.format(str(user_answer), str(correct_answer)))
            print('Let\'s try again')
            return
    print('Congratulations! You win!')
