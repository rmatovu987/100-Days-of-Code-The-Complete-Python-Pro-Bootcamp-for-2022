from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for qtn in question_data:
    question_bank.append(Question(qtn['question'], qtn['correct_answer']))

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print(f"You've completed the quiz. Your final score is {brain.score}/{brain.question_number}")
