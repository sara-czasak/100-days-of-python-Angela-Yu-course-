from tkinter import *
from tkinter import messagebox

from quiz_brain import *
from quiz_data import *


# CONSTANTS
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
CORRECT = 'green'
INCORRECT = 'red'


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        # Score text
        self.score_label = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg='white', font=FONT)
        self.score_label.grid(column=1, row=0)

        # Question canvas
        self.canvas = Canvas(self.window, width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, text="Some question text", font=FONT, width=280)


        # Create buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)


        # Get first questio
        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(
            self.question_text, text=q_text)


    def check_answer_true(self):
        score, is_correct = self.quiz.check_answer('True')
        self.score_label.config(text=f'Score: {score}')

        if is_correct:
            self.window.config(bg=CORRECT)
            self.score_label.config(bg=CORRECT)
            self.window.after(500, self.change_back)
        else:
            self.window.config(bg=INCORRECT)
            self.score_label.config(bg=INCORRECT)
            self.window.after(500, self.change_back)

        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')
            self.play_again()


    def check_answer_false(self):
        score, is_correct = self.quiz.check_answer('False')
        self.score_label.config(text=f'Score: {score}')

        if is_correct:
            self.window.config(bg=CORRECT)
            self.score_label.config(bg=CORRECT)
            self.window.after(500, self.change_back)
        else:
            self.window.config(bg=INCORRECT)
            self.score_label.config(bg=INCORRECT)
            self.window.after(500, self.change_back)

        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')
            self.play_again()


    def change_back(self):
        self.window.config(bg=THEME_COLOR)
        self.score_label.config(bg=THEME_COLOR)


    def play_again(self):
        play_again = messagebox.askquestion("Play again", "Would you like to play again?")
        if play_again == "no":
            self.window.destroy()
        else:
            self.reset_game()


    def reset_game(self):
        new_data = get_data()
        self.quiz = QuizBrain(new_data)
        self.score_label.config(text="Score: 0")
        self.true_button.config(state='normal')
        self.false_button.config(state='normal')
        self.get_next_question()



if __name__ == '__main__':
    print('ui.py is running')
    quiz_interface = QuizInterface(QuizBrain(get_data()))