import random


PROGRESSION_LENGTH = 10
GAME_RULES = 'What number is missing in the progression?'


def get_progression(first_member, difference, length):
    progression = []
    member = first_member

    for n in range(length):
        progression.append(str(member))
        member += difference

    return progression


def get_question(progression, lost_position):
    progression[lost_position] = '..'
    progression = ' '.join(progression)

    return progression


def generate_question_answer():
    first_member = random.randint(1, 10)
    difference = random.randint(1, 10)
    lost_position: int = random.randint(1, PROGRESSION_LENGTH - 1)
    progression: list[int] = get_progression(
        first_member,
        difference,
        PROGRESSION_LENGTH
    )
    answer = progression[lost_position]
    question = get_question(progression, lost_position)

    return question, answer
