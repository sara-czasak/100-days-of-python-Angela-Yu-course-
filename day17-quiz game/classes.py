from quiz_data import *


class ScoreBoard:
    def __init__(self, question_total, question_bank):
        self.question_total = question_total
        self.question_bank = question_bank
        self.question_text = [i['question'] for i in question_bank]
        self.correct_answer = [i["correct_answer"] for i in question_bank]


    def check_answer(self, answer, question, score):
        correct = self.correct_answer[self.question_text.index(question)]
        print(correct)
        if answer == correct:
            score += 1
            self.increase_score(score)
        else:
            self.increase_score(score)


    def increase_score(self, score):
        score += 1
        return score


    def display_score(self, score):
        return f"Score: {score} / {self.question_total}"



scoreboard = ScoreBoard(15, quiz_data)
# print(scoreboard.display_score('1'))