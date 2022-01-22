import random

FIRST_VALUE_RANGE = 1
SECOND_VALUE_RANGE = 100
GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(value):
    return value % 2 == 0


def generate_question_answer():
    quetion = random.randint(FIRST_VALUE_RANGE, SECOND_VALUE_RANGE)
    answer = 'yes' if is_even(quetion) else 'no'
    return quetion, answer
