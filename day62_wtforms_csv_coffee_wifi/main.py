import os.path

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import URLField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class CafeForm(FlaskForm):
    open_time_choices = [("8AM", "8AM"), ("8:30AM", "8:30AM"), ("9:00AM", "9:00AM"), ("9:30AM", "9:30AM"), ("10AM", "10:30AM")]
    close_time_choices = [("8PM", "8PM"), ("8:30PM", "8:30PM"), ("9:00PM", "9:00PM"), ("9:30PM", "9:30PM"),
                         ("10PM", "10:30PM")]
    coffee_rating_choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
    wifi_rating_choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
    power_socket_choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]


    cafe_name = StringField(label='Cafe Name', validators=[DataRequired()])
    cafe_location = URLField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    cafe_open_time = SelectField(label='Opening Time (e.g. 8AM)', choices=open_time_choices, validators=[DataRequired()])
    cafe_close_time = SelectField(label='Closing Time (e.g. 5:30PM)', choices=close_time_choices, validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", choices=coffee_rating_choices, validators=[DataRequired()])
    wifi_strength_rating = SelectField(label="Wifi Strength Rating", choices=wifi_rating_choices,validators=[DataRequired()])
    power_socket = SelectField(label="Power Socket Availability", choices=power_socket_choices, validators=[DataRequired()])
    submit = SubmitField(label='Submit')



# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if form.validate_on_submit() and request.method == "POST":
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe_name.data},"
                           f"{form.cafe_location.data},"
                           f"{form.cafe_open_time.data},"
                           f"{form.cafe_close_time.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_strength_rating.data},"
                           f"{form.power_socket.data}")
        return redirect(url_for('cafes'))
        # form_data = form.data
        #
        # #Remove the Submit field from the data returnbed
        # form_data.pop("submit", None)
        # form_data.pop("csrf_token", None)
        #
        # form_values = []
        # for field_name, value in form.data.items():
        #     form_values.append(value)
        #
        # with open("cafe-data.csv", "a", newline="") as file:
        #    writer = csv.writer(file, delimiter=",")
        #    writer.writerow(form_values)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
