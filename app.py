import os
from flask import Flask, render_template

app = Flask(__name__)

"""
Whenever 'route' is called (the directory)
the index() function is also called due to 
@app decorator. The index() function
can also be called 'a view' and it is 'binded'
to the decorator directly above it
"""
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), # gets IP address, and sets default if not found
        port=int(os.environ.get("PORT", "5000")),
        debug=True)