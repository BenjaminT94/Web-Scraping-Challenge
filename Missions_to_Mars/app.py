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
    return render_template("index.html",dict=Mars_dict)