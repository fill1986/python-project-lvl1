#!/usr/bin/env python

import random
from brain_games.engine import engine


rules_game = 'What is the result of the expression?'


def generate_Question_Answer():
    signs = ['-', '+', '*']
    first_sign = 0
    last_sign = len(signs) - 1
    random_sign = random.randint(first_sign, last_sign)

    first_value_range = 1
    second_value_range = 10
    operand_1 = random.randint(first_value_range, second_value_range)
    operand_2 = random.randint(first_value_range, second_value_range)

    if signs[random_sign] == '-':
        return (f'{operand_1} - {operand_2}', operand_1 - operand_2)
    elif signs[random_sign] == '+':
        return (f'{operand_1} + {operand_2}', operand_1 + operand_2)
    elif signs[random_sign] == '*':
        return (f'{operand_1} * {operand_2}', operand_1 * operand_2)


def main():

    engine(generate_Question_Answer, rules_game)


if __name__ == '__main__':
    main()
