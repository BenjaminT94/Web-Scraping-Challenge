# Dependencies
from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    Mars_collection = mongo.db.Mars_dict.find_one()
    return render_template("index.html",mars=Mars_collection)
@app.route("/scrape")
def scrape():

    # Scrape
    Mars_dict = scrape_mars.scrape()
    mongo.db.Mars_dict.update({},Mars_dict,upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
