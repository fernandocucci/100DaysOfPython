class QuizBrain:
    def __init__(self, question_bank):
        self.current_question = 0
        self.question_bank = question_bank
        self.score = 0

    def next_question(self):
        current_text = self.question_bank[self.current_question].text
        current_answer = self.question_bank[self.current_question].answer
        self.current_question += 1
        user_answer = (input(f"Q.{self.current_question} {current_text} (True/False): ")).lower()
        if current_answer.lower() == user_answer:
            print(f"You got it right, the answer was: {user_answer}")
            self.score += 1
        else:
            print(f"That is not correct, the answer was: {current_answer}")
        print(f"Your current score is: {self.score} / {self.current_question}")

    def has_questions(self):
        return self.current_question < len(self.question_bank)
