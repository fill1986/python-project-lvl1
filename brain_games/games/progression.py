import random


PROGRESSION_LENGTH = 10
GAME_RULES = 'What number is missing in the progression?'


def get_progression():
    progression = []
    first_member_progression = random.randint(1, 10)
    difference_progression = random.randint(1, 10)
    member_progression = first_member_progression

    for n in range(PROGRESSION_LENGTH):
        progression.append(str(member_progression))
        member_progression += difference_progression

    return progression


def get_question(list_progression, lost_position):
    list_progression[lost_position] = '..'
    list_progression = ' '.join(list_progression)

    return list_progression


def generate_question_answer():
    lost_position_progression = random.randint(1, PROGRESSION_LENGTH - 1)
    progression_list = get_progression()
    answer = progression_list[lost_position_progression]
    question = get_question(progression_list, lost_position_progression)

    return question, answer
