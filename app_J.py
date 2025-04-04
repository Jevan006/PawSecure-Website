from flask import Flask, render_template

from configurations import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/qoutes")
def qoutes():
    return render_template("qoutes_page.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
