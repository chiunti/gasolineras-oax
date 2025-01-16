from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def gasolineras():
    return render_template("Gasolineras.html")
