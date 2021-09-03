# Dependencies
from flask import Flask, render_template
import pymongo
import scrape_mars

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db=client.mars_db



@app.route("/")
def home():
    Mars_dict = db.Mars_dict.find_one()
    # Return template and data
    return render_template("index.html", mars=Mars_dict)
@app.route("/scrape")
def scrape():
    Mars_dict = db.Mars_dict
    mars_data = scrape_mars.scrape()
    dict.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)