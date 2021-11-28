#!/usr/bin/env python

import random
from brain_games.cli import welcome_user
import prompt


def summa(value_1, value_2):
    return ('+', value_1 + value_2)


def difference(value_1, value_2):
    return ('-', value_1 - value_2)


def multiplication(value_1, value_2):
    return ('*', value_1 * value_2)


def main():
    def game_calulator():
        name_player = welcome_user()
        win_value = 0
        while win_value != 3:
            print('What is the result of the expression?')
            for operation in [summa, difference, multiplication]:
                operand_1 = random.randint(1, 10)
                operand_2 = random.randint(1, 10)
                question = operation(operand_1, operand_2)
                sign = question[0]
                answer = question[1]
                print(f'Question: {operand_1} {sign} {operand_2}')
                answer_user = prompt.integer('Your answer: ')

                if answer != answer_user:
                    print(f"{answer_user} is wrong answer ;(. Correct {answer}")
                    print(f"Let's try again, {name_player}")
                    return 0
                print('Correct!')
                win_value += 1

        print(f'Congratulations, {name_player}')

    game_calulator()


if __name__ == '__main__':
    main()
