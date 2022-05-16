# ==========================================
# Day 017 - Project: Quiz Brain Trivia
# ==========================================

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q = Question(question["text"], question["answer"])
    question_bank.append(q)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.has_questions():
    quiz_brain.next_question()

print(f"Your final score is: {quiz_brain.score}")

