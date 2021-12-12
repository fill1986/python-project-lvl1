#!/usr/bin/env python

import random
from brain_games.engine import engine


rules_game = 'What number is missing in the progression?'


def generate_Question_Answer():
    first_value_progression = random.randint(1, 10)
    current_value_progression = first_value_progression
    step_progression = random.randint(1, 10)
    lost_position_progression = random.randint(1, 10)
    progression = ''
    answer = 0
    i = 0

    while i <= 10:
        if i == lost_position_progression:
            progression += ' ..'
            answer = str(current_value_progression)
        else:
            progression += f' {current_value_progression}'
        current_value_progression += step_progression
        i += 1

    return (progression, answer)


def main():

    engine(generate_Question_Answer, rules_game)


if __name__ == '__main__':
    main()
