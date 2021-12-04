#!/usr/bin/env python

from math import sqrt
import random
from brain_games.cli import welcome_user
import prompt


def is_prime(value):
    if value <= 1:
        return 'no'
    i = 2
    while i <= sqrt(value):
        if value % i == 0:
            return 'no'
        i += 1
    return 'yes'


def main():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def game_prime():
        name_player = welcome_user()
        win_value = 0
        while win_value != 3:
            print(rules)
            quetion = random.randint(1, 100)
            print(f'Question: {quetion}')
            answer = prompt.string('Your answer: ')
            true_answer = is_prime(quetion)

            if true_answer != answer:
                print(f"'{quetion} is wrong answer ;(. Correct answer was 'no'")
                return 0
            print('Correct!')
            win_value += 1

        print(f'Congratulations, {name_player}')

    game_prime()


if __name__ == '__main__':
    main()
