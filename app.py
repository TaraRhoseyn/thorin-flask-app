import os
from flask import Flask, render_template

app = Flask(__name__)

"""
Whenever 'route' is called (the directory)
the index() function is also called due to 
@app decorator
"""
@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), # gets IP address, and sets default if not found
        port=int(os.environ.get("PORT", "5000")),
        debug=True)