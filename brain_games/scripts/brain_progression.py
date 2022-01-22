#!/usr/bin/env python

from brain_games.games.progression import generate_question_answer, GAME_RULES
from brain_games.engine import start_game


def main():

    start_game(generate_question_answer, GAME_RULES)


if __name__ == '__main__':
    main()
