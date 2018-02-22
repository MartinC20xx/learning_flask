from flask import render_template
from app import app
from systeminfo import main
#added import for testing reasons

@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'Martin'
    returnDict['title'] = 'Home'
   
    return render_template("index.html", **returnDict)
