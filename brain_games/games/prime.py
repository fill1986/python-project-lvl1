from math import sqrt
import random

FIRST_VALUE_RANGE = 1
SECOND_VALUE_RANGE = 100
GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(value):
    if value <= 1:
        return False
    i = 2
    while i <= sqrt(value):
        if value % i == 0:
            return False
        i += 1
    return True


def generate_question_answer():
    quetion = random.randint(FIRST_VALUE_RANGE, SECOND_VALUE_RANGE)
    answer = 'yes' if is_prime(quetion) else 'no'
    return quetion, answer
