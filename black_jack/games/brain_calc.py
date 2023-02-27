import random


RULES = 'What is the result of the expression?'


def find_correct_answer(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number


def generate_round():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    correct_answer = find_correct_answer(first_number, second_number, operation)
    question = f'{first_number} {operation} {second_number}'
    return question, correct_answer
