import random


def is_even(value):
    return value % 2 == 0


def generate_question_answer():
    first_value_range = 1
    second_value_range = 100
    quetion = random.randint(first_value_range, second_value_range)
    answer = 'yes' if is_even(quetion) else 'no'
    return quetion, answer
