from random import randint


RULES = 'What number is missing in the progression?'


def generate_round():
    length_progression = randint(5, 10)
    start = randint(1, 10)
    step = randint(1, 10)
    secret_number = randint(0, length_progression - 1)
    question = ' '
    progression = [f'{start}', f'{start + step}', f'{start + step * 2}',
                   f'{start + step * 3}', f'{start + step * 4}',
                   f'{start + step * 5}', f'{start + step * 6}',
                   f'{start + step * 7}', f'{start + step * 8}',
                   f'{start + step * 9}']
    progression[secret_number] = '..'
    question = question.join(progression)
    correct_answer = str(start + (step * secret_number))
    return question, correct_answer
