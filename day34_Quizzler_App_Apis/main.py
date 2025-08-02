"""
    CONCEPTS:  Refresher on Classes, TKinter (Used to create GUIs)

    New Concept: Type Hints
    -- specifying the data type and the return type of a variable or function so that the IDE
       will provide "hints" when the variable value or function return value does not match the specified data type
       -- Syntax:
            -- for variable: `varName: dataType`
                i.e. name: str
            -- for return type:  `-> returnType`
                i.e.  def foo(name:str) -> str:
                        return 'Hello' + name

"""

from ui import QuizInterface
from question_model import Question
from data import question_data, random_category
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz, random_category)

# commented out to work with the QuizInterface class (ui.py).  Class implements TKinter object and TKinter uses window.mainloop.
# Cannot run another "while" loop when using TKInter "mainloop"

# while quiz.still_has_questions():
#     quiz.next_question()


