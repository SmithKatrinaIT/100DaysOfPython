"""
    CONCEPT: Build RESTful API
        Previous modules covered using other companies APIs, we are building our own apis

        -- What is REST: REpresentational State Transfer
            -- Based off the Client ---> Server Architecture
                -- Client makes a request to an endpoint via the internet (i.e http, https, ftp, soap)
                -- Server responses to the request either by providing the requested information or with an error code
                -- APIs: are a bunch of services that can be exposed to clients to be able to tap into to request information

        -- What is it to make an API RESTful
            -- RESTful is an architectural style: it is a way of constructing/designing an api
            -- A RESTFul api has to follow specific rules (here are 2 main ones)
                -- must use HTTP Request verbs
                    -- Verbs: GET, POST, PUT, PATCH, DELETE
                -- must specific pattern of routes/endpoint URLs
                    -- Routes: /home, /articles

        -- RESTful APIs are in JSON (JavaScript Object Notation) form
            -- "Key": "Value" --- pairs

            -- Process of converting db string data into JSON is called "serialization"
            -- "jsonify()": Flask serialization helper built-in method




"""
import os
from dotenv import load_dotenv
import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask_bootstrap import Bootstrap5

# Load ENV variables
load_dotenv("../.env")


'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2. Alternatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random', methods=["GET"])
def get_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)

    # Debug: test if DB results are returned
    #return render_template("index.html", cafe=result)

    """ Return Method 1 """
    # return jsonify(cafe={
    #     "id": result.id,
    #     "name": result.name,
    #     "map_url": result.map_url,
    #     "img_url": result.img_url,
    #     "location": result.location,
    #     "seats": result.seats,
    #     "has_toilet": result.has_toilet,
    #     "has_wifi": result.has_wifi,
    #     "has_sockets": result.has_sockets,
    #     "can_take_calls": result.can_take_calls,
    #     "coffee_price": result.coffee_price,
    # })

    """ Return Method 2: Simply convert the random_cafe data record to a dictionary of key-value pairs.  """
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=['GET'])
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


# HTTP GET - Read Record
@app.route("/search", methods=['GET'])
def get_search_cafes():
    # request.args.get() is used to retrieve values from a URL's query string—the part of a URL after the ? mark
    query_location = request.args.get("loc")

    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    filtered_cafes = result.scalars().all()

    if filtered_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in filtered_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"}), 404


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_cafe():

    "The Key-Value pairs you enter into the Body tab in Postman is equivalent to <input> elements. Thus, we use `request.form.get` instead of `request.args.get`"
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"))

    exists = Cafe.query.filter_by(name=new_cafe.name).first()

    if exists:
        return jsonify(response={"Bad Request": "Cafe already exists"}), 400
    else:

        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."}), 200


# HTTP PUT/PATCH - Update Record
""" Difference between PUT and PATCH
    PUT: updating the entire record
    PATCH: only update the specific pieces of data
"""
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def get_cafe_by_id(cafe_id):

    new_price = request.args.get("coffee_price")
    api_key = os.getenv("API_KEY")
    try:

        # Method 1: to retrieve DB record by ID
        #cafe_to_update = Cafe.query.filter_by(id=cafe_id).first()

        # Method 2: to retrieve DB record by ID
        cafe = db.session.get(Cafe, cafe_id)
        print(f"cafe get returned: {cafe}")

        if cafe and new_price:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."}), 200

        else:
            return jsonify(response={"error": "Cafe doesn't exist or coffee price not provided"}), 404

    except AttributeError as err:
        msg = f"[{err}]:No Cafe with that id present."
        return jsonify(response={"Bad Request": msg})


# HTTP DELETE - Delete Record
@app.route("/delete/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):

    key = request.args.get("api-key")
    api_key = os.environ.get("API_KEY")

    try:
        cafe = db.session.get(Cafe, cafe_id)
        print(f"cafe from db: {cafe}")

        if key == api_key:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Cafe successfully deleted"}), 200
        else:
            return jsonify(response={"error": "Sorry, that is not allowed. Make sure you have the correct API KEY"}), 403
    except Exception as e:
        msg = f"[{e}]: Sorry unabled to process your request."
        return jsonify(response={"error": msg}), 500


if __name__ == '__main__':
    app.run(debug=True)
