from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank =[]
for i in question_data:
    q_text= i["text"]
    ans= i["answer"]
    new_question = Question(q_text,ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()

print("Game over!")
print(f"Your final score is {quiz.score}/{quiz.question_num}")

