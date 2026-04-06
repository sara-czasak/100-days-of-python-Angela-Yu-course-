# from classes import *
from quiz_data import *
from ui import *
from quiz_brain import *


total_questions = len(get_data())

quiz_brain = QuizBrain(get_data())
quiz_ui = QuizInterface(quiz_brain)


