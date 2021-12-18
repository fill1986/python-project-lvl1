#!/usr/bin/env python

import random
from brain_games.engine import engine

rules_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(value):
    if value % 2 == 0:
        return True
    return False


def generate_Question_Answer():
    first_value_range = 1
    second_value_range = 100
    quetion = random.randint(first_value_range, second_value_range)
    answer = 'yes' if is_even(quetion) else 'no'
    return (quetion, answer)


def main():

    engine(generate_Question_Answer, rules_game)


if __name__ == '__main__':
    main()
