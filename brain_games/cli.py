import prompt

number_of_rounds = 3

def run_app(rounds):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    template = 'Hello, {}'
    print(template.format(name))
