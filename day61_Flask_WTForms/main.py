'''
    CONCEPT:  Adding Bootstrap

'''



import os

from flask import Flask, render_template, request
from day61_Flask_WTForms.contact_form import ContactForm
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../.env")


app = Flask(__name__)
app.secret_key = os.environ.get("WTFORMS_SECRET_KEY")
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = ContactForm()
    form.validate_on_submit()

    if form.validate_on_submit() and request.method == "POST":
        if form.email.data == "admin@email.com" and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')


    return render_template('login.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)
