import random

GAME_RULES = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 1
UPPER_BOUND = 20


def calculate_gcd(value_1, value_2):
    while value_1 != 0 and value_2 != 0:
        if value_1 >= value_2:
            value_1 %= value_2
        else:
            value_2 %= value_1
    return value_1 or value_2


def generate_question_answer():
    '''
    value_1, value_2 в константы на уровень модуля не выношу,
    тк на каждом шагу нужно генерить новое значение
     '''
    value_1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    value_2 = random.randint(LOWER_BOUND, UPPER_BOUND)
    answer = calculate_gcd(value_1, value_2)

    return f"{value_1} {value_2}", answer
