"""
Concept: classes OPP
 -- Creating a Quiz program
"""

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{self.question_number}")

    # TODO: asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False)? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print(f"Sorry, that is wrong")
        print(f"Correct answer is {correct_answer.capitalize()}.")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")







    # TODO: checking if the answer was correct

    # TODO: checking if at the end of quiz