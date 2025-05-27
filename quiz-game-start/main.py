from question_model import Question
from data import question_data

question_bank =[]
for i in question_data:
    q_text= i["text"]
    ans= i["answer"]
    new_question = Question(q_text,ans)
    question_bank.append(new_question)

print(question_bank[1].text)

