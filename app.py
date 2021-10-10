import os
import json
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
    data = []
    with open("data/company.JSON", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)

@app.route("/about/<member_name>")
def about_member(member_name):
    member = {} # empty object for now
    with open("data/company.JSON", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj 
    return render_template("member.html", member=member)

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), # gets IP address, and sets default if not found
        port=int(os.environ.get("PORT", "5000")),
        debug=True)