class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_question(self):
        return self.question_num < len(self.question_list)
        

        # question = self.question_list[self.question_num]
        # if question.answer == self.usr_ip:
        #    return True 
        # else:
        #     return False

    def next_question(self):
        question = self.question_list[self.question_num]
        self.question_num += 1
        usr_ip = input(f"Q {self.question_num}: {question.text}. (True/False)?:")
        self.check_answer(usr_ip,question.answer)
    

    def check_answer(self, usr_ans, correct_ans):
        if usr_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_num}")
        