from flask import Flask, render_template, request, redirect, url_for, flash, session
from contact_me import send_contact_email
from projects import morse_code_converter as mc
from forms import MorseCodeForm, QuizForm
from projects.quizzler.trivia_service import get_questions
import os
from dotenvx import load_dotenv

load_dotenv("../../.env")

app = Flask(__name__)
app.secret_key["SECRET_KEY"] = os.environ.get("PORTFOLIO_SEC_KEY")


@app.route("/")
def home():
    return render_template("index.html", page="home")


@app.route("/about")
def about():
    return render_template("about.html", page="about")


@app.route("/projects")
def projects():
    return render_template("projects.html", page="projects")


@app.route("/services")
def services():
    return render_template("services.html", page="services")


@app.route("/resume")
def resume():
    return render_template("resume.html", page="resume")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":

        form_data = {
            'name': request.form['name'].strip(),
            'email': request.form['email'].strip(),
            'subject': request.form['subject'].strip(),
            'message': request.form['message'].strip()
        }

        if send_contact_email(form_data):
            flash("Success! Your message has been sent successfully.", "success")
        else:
            flash("Error: Could not send your message.","danger")
        return redirect(url_for("contact"))

    return render_template("contact.html", page="contact")


@app.route("/interactive-projects/morse-code-project", methods=["GET", "POST"])
def morse_code_project():
    form = MorseCodeForm()
    result = None

    if form.validate_on_submit():

        msg_input = form.message.data
        conversion_type = form.conversion_type.data

        if conversion_type == "text_to_morse":
            result = mc.text_to_morse(msg_input)

        elif conversion_type == "morse_to_text":
            result = mc.morse_to_text(msg_input)

    return render_template("morse_code_project.html", form=form, result=result, page="projects", active_project="morse")

@app.route("/interactive-projects/quizzler", methods=["GET", "POST"])
def quizzler_project():
    form = QuizForm()

    # Start New Quiz
    if "quiz_questions" not in session:
        question_bank, category = get_questions()
        session["quiz_questions"] = [
            {
                "text": question.text,
                "answer": question.answer
            }
            for question in question_bank
        ]

        session["quiz_category"] = category
        session["quiz_question_number"] = 0
        session["quiz_score"] = 0

    questions = session["quiz_questions"]
    question_number = session["quiz_question_number"]
    score = session["quiz_score"]
    category = session["quiz_category"]

    # Process answer
    feedback = None
    answer_correct = None

    if form.validate_on_submit():
        current_question = questions[question_number]
        if form.true.data:
            user_answer = "True"
        else:
            user_answer = "False"

        answer_correct = (user_answer.lower() == current_question["answer"].lower() )

        if answer_correct:
            score += 1
            session["quiz_score"] = score
            feedback = "Correct!"
        else:
            feedback = "Incorrect."

        question_number += 1
        session["quiz_question_number"] = question_number

    # Determine whether quiz is over

    quiz_complete = (question_number >= len(questions))

    if quiz_complete:
        question = None
    else:
        question = questions[question_number]

    return render_template(
        "quizzler_project.html",
        form=form,
        question=question,
        question_number=question_number,
        total_questions=len(questions),
        score=score,
        category=category,
        feedback=feedback,
        answer_correct=answer_correct,
        quiz_complete=quiz_complete,
        active_project="quizzler"
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5001))
    host = os.environ.get("FIGMA_DEV_SERVER_HOST", "0.0.0.0")
    app.run(debug=True, host=host, port=port)

