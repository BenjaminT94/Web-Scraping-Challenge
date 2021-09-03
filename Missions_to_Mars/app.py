# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")



@app.route("/")
def home():
    Mars_dict = mongo.db.Mars_dict.find_one()
    # Return template and data
    return render_template("index.html", mars=Mars_dict)
@app.route("/scrape")
def scrape():
    Mars_dict = mongo.db.Mars_dict
    mars_data = scrape_mars.scrape()
    dict.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)