import prompt
from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def start_game(get_question_answer, game_rules):
    player_name = welcome_user()
    print(game_rules)

    for n in range(ROUNDS_COUNT):
        question, answer = get_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if str(answer) == user_answer:
            print('Correct!')
        else:
            msg_wrong_answer = 'is wrong answer ;(. Correct answer was'
            print(f"'{user_answer}' {msg_wrong_answer} '{answer}'.")
            print(f"Let's try again, {player_name}!")
            return

    print(f'Congratulations, {player_name}!')
