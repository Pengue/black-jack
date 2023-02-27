import random
from brain_games.games.brain_even import compare_answer


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    elif a == 1:
        return False
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def generate_round():
    question = random.randint(1, 100)
    correct_answer = compare_answer(is_prime(question))
    return question, correct_answer
