from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/matheus")
def matheus():
    return "Olá, Matheus"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Olá, {name}"