import random

LOWER_BOUND = 1
UPPER_BOUND = 100
GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(value):
    return value % 2 == 0


def generate_question_answer():
    quetion = random.randint(LOWER_BOUND, UPPER_BOUND)
    answer = 'yes' if is_even(quetion) else 'no'
    return quetion, answer
