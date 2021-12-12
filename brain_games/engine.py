import prompt
from brain_games.cli import welcome_user


def cheak_answer(answer, user_answer):
    if str(answer) == user_answer:
        return True
    return False


def engine(get_Question_Answer, rules_game):
    count_rounds = 3
    name_player = welcome_user()
    print(rules_game)

    while count_rounds > 0:
        question, answer = get_Question_Answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if cheak_answer(answer, user_answer):
            print('Correct')
            count_rounds -= 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}")
            print(f"Let's try again, {name_player}!")
            return 0

    print(f'Congratulations, {name_player}!')
