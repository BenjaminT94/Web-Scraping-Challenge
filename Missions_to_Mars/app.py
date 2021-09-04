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
    Mars_dict = mongo.db.Mars_dict.find_one()
    return render_template("index.html",mars=Mars_dict)
@app.route("/scrape")
def scrape():

    # Run the scrape function
    Mars_dict = mongo.db.Mars_dict
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    Mars_dict.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
