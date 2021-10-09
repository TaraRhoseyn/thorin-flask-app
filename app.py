import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello</h1> <h2>world</h2>"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), # gets IP address, and sets default if not found
        port=int(os.environ.get("PORT", "5000")),
        debug=True)