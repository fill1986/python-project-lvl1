#!/usr/bin/env python

from math import sqrt
import random
from brain_games.engine import engine

rules_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(value):
    if value <= 1:
        return False
    i = 2
    while i <= sqrt(value):
        if value % i == 0:
            return False
        i += 1
    return True


def generate_Question_Answer():
    first_value_range = 1
    second_value_range = 100
    quetion = random.randint(first_value_range, second_value_range)
    answer = 'yes' if is_prime(quetion) else 'no'
    return (quetion, answer)


def to_start():

    engine(generate_Question_Answer, rules_game)
