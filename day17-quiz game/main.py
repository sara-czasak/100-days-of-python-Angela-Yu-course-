from classes import *
from quiz_data import *


total_questions = len(quiz_data)


score = 0
score_board = ScoreBoard(total_questions, quiz_data)

print("*** WELCOME TO THE QUIZ ***")
print("-" * 20)
print('Are you ready to be quizzed? (y/n) ')
start = input().lower()
start = score_board.check_if_start(start)
# ready = False
# while not ready:
#     if start.startswith('y'):
#         ready = True
#     elif start.startswith('n'):
#         ready = True
#     else:
#         print('Please enter either "y" or "n"')
#         start = input().lower()


if start:
    print("*** LET'S PLAY! ***")
    game_on = True
else:
    print("*** SEE YOU NEXT TIME! ***")
    game_on = False


counter = 0
score = 0

while game_on:
    if counter <= total_questions - 1:
        print("\n*** TRUE or FALSE ***")
        question, currect_answer = score_board.display_question(counter)
        print(question)
        answer = input().lower()
        answered = False
        while not answered:
            if answer.startswith('t'):
                answer = 'True'
                answered = True
            elif answer.startswith('f'):
                answer = 'False'
                answered = True
            else:
                print('Please enter either "t" or "f"')
                answer = input().lower()
        if score_board.check_answer(answer, currect_answer):
            score = score_board.increase_score(score)
        print(f"SCORE: {score}/{total_questions}")
        counter += 1
    else:
        print("*** CONGRATULATIONS, YOU FINISHED THE QUIZ ***")
        print(f"*** YOUR FINAL SCORE IS  {score} OUT OF {total_questions} ***")
        print("-" * 20)
        print('Would you like to play again? (y/n)')
        start = input().lower()
        start = score_board.check_if_start(start)

