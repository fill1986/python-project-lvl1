#!/usr/bin/env python

import random
from brain_games.cli import welcome_user
import prompt


def generate_progression():
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
            answer = current_value_progression
        else:
            progression += f' {current_value_progression}'
        current_value_progression += step_progression
        i += 1

    return (progression, answer)


def main():

    def game_progression():
        name_player = welcome_user()
        win_value = 0
        while win_value != 3:
            print('What number is missing in the progression?')
            progression, answer = generate_progression()
            print(f'Question: {progression}')
            answer_user = prompt.integer('Your answer: ')

            if answer != answer_user:
                print(f"{answer_user} is wrong answer ;(. Correct {answer}")
                print(f"Let's try again, {name_player}")
                return 0
            print('Correct!')
            win_value += 1

        print(f'Congratulations, {name_player}')

    game_progression()


if __name__ == '__main__':
    main()
