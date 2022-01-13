#!/usr/bin/env python

from brain_games.games.gcd import generate_question_answer
from brain_games.engine import start_game

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def main():

    start_game(generate_question_answer, GAME_RULES)


if __name__ == '__main__':
    main()
