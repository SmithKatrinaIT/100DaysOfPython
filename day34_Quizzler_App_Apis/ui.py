from tkinter import *
from quiz_brain import QuizBrain

# globals
THEME_COLOR = "#375362"


class QuizInterface:

	def __init__(self, quiz_brain: QuizBrain, randomcategory: QuizBrain):
		self.quiz = quiz_brain
		self.quiz_category = randomcategory["category"]
		self.window = Tk()
		self.window.title("Quizzler")
		self.window.config(padx=20, pady=20, bg=THEME_COLOR)

		# canvas properties
		self.canvas = Canvas(width=300, height=250)
		self.quiz_question = self.canvas.create_text(
			150,
			125,
			width=280,
			text="Quiz Question Goes HERE",
			font=("Arial", 20, "italic"))

		self.canvas.grid(column=0, row=1, columnspan=2, pady=(20))

		# labels
		self.score = self.quiz.score
		self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Arial", 16, "bold"))
		self.score_label.grid(column=1, row=0, pady=(20))
		self.quiz_category_label = Label(text=f"Category: {self.quiz_category.title()}", bg=THEME_COLOR, fg="white", font=("Arial", 18, "bold"))
		self.quiz_category_label.grid(column=0, row=0, pady=(20))

		#images
		wrong_img = PhotoImage(file="images/false.png")
		right_img = PhotoImage(file="images/true.png")

		# buttons
		self.wrong_btn = Button(image=wrong_img, highlightthickness=0, command=self.guess_false)
		self.wrong_btn.grid(column=1, row=2)
		self.right_btn = Button(image=right_img, highlightthickness=0, command=self.guess_true)
		self.right_btn.grid(column=0, row=2)

		#populate the canvas from quiz_brain
		self.get_next_question()


		self.window.mainloop()

	def get_next_question(self):
		self.canvas.config(bg='white')
		if self.quiz.still_has_questions():
			self.score_label.config(text=f"Score: {self.score}")
			question_text = self.quiz.next_question()
			self.canvas.itemconfig(self.quiz_question, text=question_text)

		else:
			self.canvas.itemconfig(self.quiz_question,text=f"You've completed the quiz.\nYour final score was {self.score}/{self.quiz.question_number}")
			self.right_btn.config(state="disabled")
			self.wrong_btn.config(state="disabled")

	def guess_false(self):
		correct_answer = self.quiz.check_answer("False")
		if correct_answer:
			self.score += 1
			self.canvas.config(bg='green')
			self.canvas.itemconfig(self.quiz_question, text="You guessed 'False'! You are correct")


		else:
			self.canvas.config(bg='red')
			self.canvas.itemconfig(self.quiz_question, text="You guessed 'False'! That is incorrect")

		self.score_label.config(text=f'Score: {self.score}')
		self.window.after(1000, self.get_next_question)



	def guess_true(self):
		correct_answer = self.quiz.check_answer("True")
		if correct_answer:
			self.score += 1
			self.canvas.config(bg='green')
			self.canvas.itemconfig(self.quiz_question, text="You guessed 'TRUE'!\nThat is correct")
		else:
			self.score = self.score
			self.canvas.config(bg='red')
			self.canvas.itemconfig(self.quiz_question, text="You guessed 'True'!\nThat is incorrect")

		#self.score_label.config(text=f'Score: {self.score}')
		self.window.after(2000, self.get_next_question)


