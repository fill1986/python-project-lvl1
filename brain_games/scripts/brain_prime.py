#!/usr/bin/env python

from brain_games.games.prime import generate_question_answer
from brain_games.engine import start_game

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():

    start_game(generate_question_answer, GAME_RULES)


if __name__ == '__main__':
    main()
