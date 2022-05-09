class QuizBrain:
    """The Quiz brain class"""

    def __init__(self, q_list):
        """Class constructor"""
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        """Method to go to the next question"""
        qtn = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f'Q.{self.question_number}: {qtn.text} : (True/False) ')
        self.check_answer(qtn, ans)

    def still_has_questions(self) -> bool:
        """Method to determine if the question list still has questions"""
        return self.question_number < len(self.question_list)

    def check_answer(self, qtn, answer):
        """Check if the answer is correct"""
        if qtn.answer.lower() == answer.lower():
            self.score += 1
            print('Your answer is correct')
            print(f'Your score is {self.score}/{len(self.question_list)}')
        else:
            print(f'Your answer is wrong! The answer is {qtn.answer}')
            print(f'Your score is {self.score}/{self.question_number}')
