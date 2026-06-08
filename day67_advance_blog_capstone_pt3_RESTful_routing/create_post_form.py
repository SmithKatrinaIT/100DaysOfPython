from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class CreatePostForm(FlaskForm):
    title = StringField(label='Blog Post Title', validators=[DataRequired()])
    sub_title = StringField(label='Subtitle', validators=[DataRequired()])
    author_name = StringField(label="Author's Name", validators=[DataRequired()])
    img_url = StringField(label='Background Image URL', validators=[DataRequired()])
    content = CKEditorField(label='Post Content', validators=[DataRequired()])
    submit = SubmitField(label='Submit Post')