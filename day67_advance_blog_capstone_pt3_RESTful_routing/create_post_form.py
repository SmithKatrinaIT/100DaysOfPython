from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired



class CreatePostForm(FlaskForm):

    #email = StringField(label='Email',render_kw={"placeholder": "Enter Email"})
    title = StringField(label='Blog Post Title', validators=[DataRequired()])
    sub_title = StringField(label='Blog Post Subtitle', validators=[DataRequired()])
    author_name = StringField(label='Blog Post Subtitle', validators=[DataRequired()])
    img_url = StringField(label='Background Image URL', validators=[DataRequired()])
    content = CK(label='Blog Post Subtitle', validators=[DataRequired()])
    submit = SubmitField(label='Add Post')