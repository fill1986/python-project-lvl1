#!/usr/bin/env python

import random
from brain_games.cli import welcome_user
import prompt


def main():

    def is_even(value):
        if value % 2 == 0:
            return 'yes'
        return 'no'

    def game_even():
        print("Welcome to the Brain Games")
        name_player = welcome_user()
        win_value = 0
        while win_value != 3:
            print('Answer "yes" if the number is even, otherwise answer "no".')
            quetion = random.randint(1, 100)
            print(f'Question: {quetion}')
            answer = prompt.string('Your answer: ')

            if is_even(quetion) != answer:
                print("'yes' is wrong answer ;(. Correct answer was 'no'")
                return 0
            print('Correct!')
            win_value += 1

        print(f'Congratulations, {name_player}')

    game_even()


if __name__ == '__main__':
    main()
