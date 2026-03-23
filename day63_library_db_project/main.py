from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
	SQLAlchemy
	-- SQLAlchemy Core is the foundational architecture for SQLAlchemy as a “database toolkit”. 
	   The library provides tools for managing connectivity to a database, interacting with database queries and results, and programmatic construction of SQL statements.
	   
	-- SQLAlchemy ORM builds upon the Core to provide optional object relational mapping capabilities. 
	   The ORM provides an additional configuration layer allowing user-defined Python classes to be mapped to database tables and other constructs, 
	   as well as an object persistence mechanism known as the Session. It then extends the Core-level SQL Expression Language to allow SQL queries 
	   to be composed and invoked in terms of user-defined objects.
	   
	   SETUP BASIC STEPS:
	   	1) imports: Flask and SQLAlchemy
	   	2) Create the Flask app: app = Flask(__name__)
	   	3) Configuration items:
	   		-- Engine or URI to the database(name): app_congig["SQLALCHEMY_ENGINES/"] = {"default": "sqlite:///db.databse_name"}
	   		-- NOTE: database used could be any db not just "sqlite:///"
	   		
	   	4) Instantiate the db object
	   		-- db = SQLAlchemy()
	   		-- db.init_app(app)
   		
'''

app = Flask(__name__)  # Create the Flask instance (application)
Bootstrap5(app)

# configure Items
app.config[
	'SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'  # configure the secret key  for cross-site Request Forgery (CSRF)
app.config[
	"SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"  # configure (add) the SQLite DB, relative to the app instance folder


# As of flask-sqlalchemy version 3.1, you need to pass a subclass of DeclarativeBase to the constructor of the database.
# create the Base object
class Base(DeclarativeBase):
	pass


# create the extension and initialize the app with the extension
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# create the table (need a lass for every table you want to create)
class Book(db.Model):
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
	author: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
	rating: Mapped[float] = mapped_column(Float, nullable=False)

	# create a string
	def __repr__(self):
		return '<Title %r>' % self.title


# create the Book Form for HTML file
class BookForm(FlaskForm):
	book_name = StringField("Book Name", [DataRequired()])
	book_author = StringField("Book Author", [DataRequired()])
	rating_choices = [(1, "1/10"), (2, "2/10"), (3, "3/10"), (4, "4/10"), (5, "5/10"), (6, "6/10"), (7, "7/10"),
					  (8, "8/10"), (9, "9/10"), (10, "10/10")]
	rating = SelectField("Rating", choices=rating_choices, validators=[DataRequired()])
	submit = SubmitField(label='Submit')

# all_books = [] # <-- Used for simple sqlite example

# create table schema
with app.app_context():
	db.create_all()


@app.route('/')
def home():
	# read all the records in the db, store in all_books object

	result = db.session.execute(db.select(Book).order_by(Book.title))
	all_books = result.scalars().all()

	db.session.connection()
	all_books_in_db = Book.query.order_by(Book.author).all()

	return render_template("index.html", books=all_books, books_db=all_books_in_db)


@app.route('/add', methods=['GET', 'POST'])
def add():
	form = BookForm()

	if form.validate_on_submit() and request.method == "POST":
		# all_books.append({
		# 	"title": form.book_name.data,
		# 	"author": form.book_author.data,
		# 	"rating": form.rating.data})

		# query the Books Collection database for unique title, per our Book class setup
		book = Book.query.filter_by(title=form.book_name.data).first()
		if book is None:
			# add book to db
			book = Book(title=form.book_name.data, author=form.book_author.data, rating=form.rating.data)
			db.session.add(book)
			db.session.commit()

			# clear form
			form.book_name.data = ""
			form.book_author.data = ""
			form.rating.data = ""

			flash("Book Added Successfully!")

		'''
		The Flask redirect() function is a built - in utility used to send a user to a different URL.It
		returns a response object with an HTTP status code that instructs the user's browser to load the new location.
		'''
		return redirect(url_for('home'))

	return render_template("add.html", form=form)


@app.route('/edit', methods=["GET", "POST"])
def edit_rating():

	if request.method == "POST":

		#update selected record
		book_id = request.form["id"]
		book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
		book_to_update.rating = request.form["rating"]
		db.session.commit()
		return redirect(url_for("home"))

	book_id = request.args.get("id")
	book_selected = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()

	return render_template("edit_rating.html", book=book_selected)


@app.route('/delete', methods=["GET", "POST"])
def delete_book():
	# delete selected record
	book_id = request.args.get('id')
	book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
	db.session.delete(book_to_delete)
	db.session.commit()
	return redirect(url_for("home"))


if __name__ == "__main__":
	app.run(debug=True)
