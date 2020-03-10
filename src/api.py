from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/generatereport/<csv>/<csv>', methods=['GET'])
def generatereport(csvtweets, csvcategories):
    #Import a csv with tweets and a csv with the categories you want tweets to be classified on

    return 

app.run("0.0.0.0", os.getenv("PORT"), debug=True)