import os
from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
    #the app is a Flask object, i suppose. 