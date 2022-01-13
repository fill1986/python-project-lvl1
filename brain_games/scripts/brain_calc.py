#!/usr/bin/env python

from brain_games.games.calc import generate_question_answer
from brain_games.engine import start_game


GAME_RULES = 'What is the result of the expression?'


def main():

    start_game(generate_question_answer, GAME_RULES)


if __name__ == '__main__':
    main()
