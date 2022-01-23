import random

UPPER_BOUND = 1
LOWER_BOUND = 10
GAME_RULES = 'What is the result of the expression?'


def generate_question_answer():
    signs = ['-', '+', '*']
    sign = random.choice(signs)
    '''
    operand_1, operand_2 в константы на уровень модуля не выношу,
    тк на каждом шагу нужно генерить новое значение
     '''
    operand_1 = random.randint(UPPER_BOUND, LOWER_BOUND)
    operand_2 = random.randint(UPPER_BOUND, LOWER_BOUND)

    if sign == '-':
        return f'{operand_1} - {operand_2}', operand_1 - operand_2
    elif sign == '+':
        return f'{operand_1} + {operand_2}', operand_1 + operand_2
    elif sign == '*':
        return f'{operand_1} * {operand_2}', operand_1 * operand_2
