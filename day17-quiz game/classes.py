from quiz_data import *


class ScoreBoard:
    def __init__(self, question_total, question_bank):
        self.question_total = question_total
        self.question_bank = question_bank
        self.question_text = [i['question'] for i in question_bank]
        self.correct_answer = [i["correct_answer"] for i in question_bank]


    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            return True
        else:
            return False


    def increase_score(self, score):
        score += 1
        return score


    def display_score(self, score):
        return f"Score: {score} / {self.question_total}"


    def display_question(self, index):
        current_question = self.question_text[index]
        current_correct_answer = self.correct_answer[index]
        return current_question, current_correct_answer


    def check_if_start(self, start):
        ready = False
        while not ready:
            if start.startswith('y'):
                ready = True
                start = True
                return start
            elif start.startswith('n'):
                ready = True
                start = False
                return start
            else:
                print('Please enter either "y" or "n"')
                start = input().lower()



scoreboard = ScoreBoard(15, quiz_data)
# print(scoreboard.display_score('1'))
