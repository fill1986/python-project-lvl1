import random


PROGRESSION_LENGTH = 10
GAME_RULES = 'What number is missing in the progression?'


def get_progression(first_member, difference, length):
    progression = []
    member_progression = first_member

    for n in range(PROGRESSION_LENGTH):
        progression.append(str(member_progression))
        member_progression += difference

    return progression


def generate_progression():
    first_member_progression = random.randint(1, 10)
    difference_progression = random.randint(1, 10)

    return get_progression(
        first_member_progression,
        difference_progression,
        PROGRESSION_LENGTH
    )


def get_question(progression: list(), lost_position_progression: int) -> str:
    progression[lost_position_progression] = '..'
    progression = ' '.join(progression)

    return progression


def generate_question_answer():
    lost_position_progression = random.randint(1, PROGRESSION_LENGTH - 1)
    progression_list = generate_progression()
    answer = progression_list[lost_position_progression]
    question = get_question(progression_list, lost_position_progression)

    return question, answer
