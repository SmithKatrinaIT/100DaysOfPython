
from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class MorseCodeForm(FlaskForm):
    conversion_type = SelectField(
        "Conversion Type",
        choices=[
            ("text_to_morse", "Text to Morse Code"),
            ("morse_to_text", "Morse Code to Text")
        ],
        validators=[DataRequired()]
    )

    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(message="Please enter a message to convert."),
            Length(max=1000)
        ]
    )

    submit = SubmitField("Convert", render_kw={"class": "btn btn-primary"})


class QuizForm(FlaskForm):
    true = SubmitField("True")
    false = SubmitField("False")