from classes import *
from quiz_data import *


total_questions = len(quiz_data)


score = 0
score_board = ScoreBoard(total_questions, quiz_data)

print("*** WELCOME TO THE QUIZ ***")
print("-" * 20)
print('Are you ready to be quizzed? (y/n) ')
start = input().lower()
ready = False
while not ready:
    if start.startswith('y'):
        ready = True
    elif start.startswith('n'):
        ready = True
    else:
        print('Please enter either "y" or "n"')
        start = input().lower()
