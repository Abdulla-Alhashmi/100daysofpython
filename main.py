from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
quiz = QuizBrain(question_bank)



for i in question_data:
    new_question = Question(i['text'], i['answer'])
    question_bank.append(new_question)

while quiz.still_has_question():
    quiz.next_question()

print("Congratulations, you completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")