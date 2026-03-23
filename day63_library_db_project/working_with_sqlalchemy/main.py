'''
	CONCEPT: DATABASES - SQLAlchemy
	-- SQLAlchemy is defined as an ORM (Object Relational Mapping) library.
	-- This means that it's able to map the relationships in the database into Objects.
	-- Fields become Object properties.
	-- Tables can be defined as separate Classes and each row of data is a new Object

	-- SQLAlchemy extension instance crates, configures, and gives access to the following things:
		-- SQLAlchemy.Model declarative model base class. It sets the table name automatically instead of needing __tablename__.
		-- SQLAlchemy.session is a session that is scoped to the current Flask application context. It is cleaned up after every request.
		-- SQLAlchemy.metadata and SQLAlchemy.metadatas gives access to each metadata defined in the config.
		-- SQLAlchemy.engine and SQLAlchemy.engines gives access to each engine defined in the config.
		-- SQLAlchemy.create_all() creates all tables.
		-- You must be in an active Flask application context to execute queries and to access the session and engine.

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# create Flask app
app = Flask(__name__)

# create the DB
class Base(DeclarativeBase):
	pass


# configure the SQLite DB, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# create the extension
db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(app)

''' As of flask-sqlalchemy version 3.1, you need to pass a subclass of DeclarativeBase to the constructor of the database.'''

# create the table
class Book(db.Model):
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
	author: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
	rating: Mapped[float] = mapped_column(Float, nullable=False)

	def __repr__(self):
		return '<Title %r>' % self.title


# create table schema
with app.app_context():
	db.create_all()

	''' Next we define and create the model. What is the : used for? Explicitly declaring a variable type. 
	Below we are explicitly saying that id is of type Mapped. 
	SQLAlchemy uses the generic Mapped so that it can type check the data that will be stored in the database.'''

# create record
with app.app_context():
	new_book = Book(id=1, title="Harry Potter", author="J.K. Rowling", rating=9.3)
	db.session.add(new_book)
	db.session.commit()

	''' NOTE: When creating new records, the primary key fields is optional. you can also write:
				new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
	the id field will be auto-generated.'''

# read all the records in the db
with app.app_context():
	result = db.session.execute(db.select(Book).order_by(Book.title))
	all_books = result.scalars()
	''' To read all the records we first need to create a "query" to select things from the database. 
	When we execute a query during a database session we get back the rows in the database (a Result object). 
	We then use scalars() to get the individual elements rather than entire rows.'''


# read a particular record by Query
with app.app_context():
	book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

	''' To get a single element we can use scalar() instead of scalars(). '''


# update a record by Primary Key
book_id = 1
with app.app_context():
	book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
	# or book_to_update = db.get_or_404(Book, book_id)
	book_to_update.title = "Harry Potter and the Goblet of Fire"
	db.session.commit()

	''' Flask-SQLAlchemy also has some handy extra query methods like get_or_404() that we can use. 
	Since Flask-SQLAlchemy version 3.0 the previous query methods like Book.query.get() have been deprecated'''


# delete a particular record by Primary key
book_id = 1
with app.app_context():
	book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
	db.session.delete(book_to_delete)
	db.session.commit()

	''' You can also delete by querying for a particular value e.g. by title or one of the other properties. Again, the get_or_404() method is quite handy.'''






