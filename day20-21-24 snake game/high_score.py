


def current_high_score():
    with open('highscore.txt', 'r') as file:
        high_score = int(file.read())
    return high_score


def save_new_high_score(new_high_score):
    with open('highscore.txt', 'w') as file:
        file.write(str(new_high_score))