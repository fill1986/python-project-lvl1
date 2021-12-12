#!/usr/bin/env python

import random
from brain_games.engine import engine

rules_game = 'Find the greatest common divisor of given numbers.'


def gsd(value_1, value_2):
    while value_1 != value_2:
        if value_1 > value_2:
            value_1 = value_1 - value_2
        else:
            value_2 = value_2 - value_1
    return value_1


def generate_Question_Answer():
    first_value_range = 1
    second_value_range = 20
    value_1 = random.randint(first_value_range, second_value_range)
    value_2 = random.randint(first_value_range, second_value_range)
    answer = gsd(value_1, value_2)

    return (f"{value_1} and {value_2}", answer)


def main():

    engine(generate_Question_Answer, rules_game)


if __name__ == '__main__':
    main()
