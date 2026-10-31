import html

class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list

    def get_question(self, question_number):

        if question_number < len(self.question_list):

            question = self.question_list[question_number]

            return {
                "text": html.unescape(question.text),
                "answer": question.answer
            }

        return None


    def check_answer(self, user_answer, correct_answer):

        return (
            user_answer.lower()
            == correct_answer.lower()
        )


