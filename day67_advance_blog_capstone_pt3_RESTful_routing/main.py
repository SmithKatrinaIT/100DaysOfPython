import datetime
import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from day67_advance_blog_capstone_pt3_RESTful_routing.create_post_form import CreatePostForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../.env")

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    result = BlogPost.query.all()

    # Method 1: for loop
    for post in result:
        posts.append(post)

    # Method 2: List comprehension
    new_list = [post for post in result]

    # using Method 1:
    # return render_template("index.html", all_posts=posts)

    # using Method 2
    return render_template("index.html", all_posts=new_list)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>', methods=["GET"])
def show_post(post_id):

    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.get(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def create_new_post():
    form = CreatePostForm()

    if form.validate_on_submit() and request.method == "POST":
        current_date = datetime.now()
        formated_date = current_date.strftime("%B %d, %Y")
        """ IMPORTANT TO REMEMBER: the variable on the left is the form field saved in the DB"""
        new_post = BlogPost(
            title=request.form.get("title"),
            subtitle=request.form.get("sub_title"),
            author=request.form.get("author_name"),
            img_url=request.form.get("img_url"),
            body=request.form.get("content"),
            date=formated_date
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)

# TODO: edit_post() to edit a blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):

    selected_post = db.session.get(BlogPost, post_id)

    edit_post_form = CreatePostForm(
        title=selected_post.title,
        sub_title=selected_post.subtitle,
        img_url=selected_post.img_url,
        author_name=selected_post.author,
        content=selected_post.body
    )

    if edit_post_form.validate_on_submit():
        selected_post.title = edit_post_form.title.data
        selected_post.subtitle = edit_post_form.sub_title.data
        selected_post.author = edit_post_form.author_name.data
        selected_post.img_url = edit_post_form.img_url.data
        selected_post.body = edit_post_form.content.data
        db.session.commit()

        return redirect(url_for("show_post", post_id=selected_post.id))


    return render_template("make-post.html", form=edit_post_form, is_edit=True)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete", methods=["GET", "POST"])
def delete_post():
    post_id = request.args.get("id")  # the variable passed in the "X" button on the index page
    post_to_delete = db.session.get(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))




# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
