from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import FloatField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
import requests

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
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass


# create the extension and initialize the app with the extension
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # create a string
    def __repr__(self):
        return '<Title %r>' % self.title

# # create table schema
# with app.app_context():
#     db.create_all()


new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, "
                    "pinned down by an extortionist's sniper rifle. Unable to leave or "
                    "receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")

another_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), "
                "the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)

    
# with app.app_context():
#     #db.session.add(new_movie)
#     db.session.add(another_movie)
#     db.session.commit()

class RateMovieForm(FlaskForm):
    # render_kw=is used specifying other form element attributes like "placeholder" ie.email = StringField(label='Email',render_kw={"placeholder": "Enter Email"})
    movie_rating = FloatField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    movie_review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class AddMovieForm(FlaskForm):
    movie_title = StringField(label='Movie Title', validators=[DataRequired()])
    movie_year = IntegerField(label="Movie Release Year")
    movie_description = StringField(label='Description', validators=[DataRequired(), Length(min=4, max=100)])
    movie_rating = FloatField(label='Rating From 1.0 to 10.0', validators=[DataRequired(), NumberRange(min=1.0, max=10.0, message="Rating cannot exceed 10.0")])
    movie_review = StringField(label="Review")
    movie_img_url = StringField(label="URL to Movie Poster Image")
    submit = SubmitField(label='Done')


@app.route("/")
def home():

    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def update_rating():

    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()

    if form.validate_on_submit() and request.method == "POST":
        movie_to_update.rating = float(form.movie_rating.data)
        movie_to_update.review = form.movie_review.data
        db.session.commit()


        # clear form
        form.movie_rating.data = ""
        form.movie_review.data = ""
        return redirect(url_for('home'))

    return render_template("edit.html", form=form, movie=movie_to_update)


@app.route("/delete", methods=["GET", "POST"])
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add_movie():

    form = AddMovieForm()
    movie_already_in_db = Movie.query.filter_by(title=form.movie_title.data).first()

    if form.validate_on_submit() and movie_already_in_db == None and request.method == "POST":

        movie_to_add = Movie(title=form.movie_title.data, year=form.movie_year.data, description=form.movie_description.data,
                      rating=form.movie_rating.data, review=form.movie_review.data, img_url=form.movie_img_url.data)

        db.session.add(movie_to_add)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)
