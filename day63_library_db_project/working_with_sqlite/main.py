'''
	CONCEPT: DATABASES - SQLITE
	-- Very popular, included with Python by default
	-- SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.
	-- The code for SQLite is in the public domain and is thus free for use for any purpose, commercial or private.

'''
import sqlite3


# create a SQLite connection
db =sqlite3.connect("books-collection.db")

# create a cursor (mouse or pointer) to control the database
cursor = db.cursor()

# create tables
# cursor.execute("CREATE TABLE books ("
# 			   "id INTEGER PRIMARY KEY,"
# 			   "title varchar(250) NOT NULL UNIQUE,"
# 			   "author varchar(250) NOT NULL,"
# 			   "rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')")
db.commit()
