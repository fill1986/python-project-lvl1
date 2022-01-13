import random


LENGH_PROGRESSION = 10


def generate_progression(lost_position):
    progression = []
    first_value = random.randint(1, 10)
    step = random.randint(1, 10)

    for n in range(LENGH_PROGRESSION):
        progression.append(str(first_value))
        first_value += step

    return progression


def make_str_progression(list_progression, lost_position):
    str_progression = ''
    list_progression.remove(list_progression[lost_position])
    list_progression.insert(lost_position, '..')
    str_progression = ' '.join(list_progression)

    return str_progression


def generate_question_answer():
    lost_position_progression = random.randint(1, LENGH_PROGRESSION - 1)
    progression_list = generate_progression(lost_position_progression)
    answer = progression_list[lost_position_progression]
    question = make_str_progression(progression_list, lost_position_progression)

    return question, answer
