#!/usr/bin/env python

import random
from brain_games.engine import engine


rules_game = 'What number is missing in the progression?'
legth_progression = 10


def generate_progression(first, step, length):
    progression = ()

    while len(progression) < length:
        progression += (first, )
        first += step

    return progression


def get_progression():
    first_value = random.randint(1, 10)
    step = random.randint(1, 10)
    length = legth_progression

    return generate_progression(first_value, step, length)


def generate_Question_Answer():
    lost_position_progression = random.randint(1, legth_progression - 1)
    tuple_progression = get_progression()
    str_progression = ''
    answer = lost_position_progression

    for (index, item) in enumerate(tuple_progression):
        if index == lost_position_progression:
            str_progression += '..'
            answer = item
        else:
            str_progression += f'{str(item)}'
        if index != len(tuple_progression) - 1:
            str_progression += " "

    return (str_progression, answer)


def main():
    engine(generate_Question_Answer, rules_game)


if __name__ == '__main__':
    main()
