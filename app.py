from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Olá, Mundo!<h1>"

@app.route("/matheus")
def matheus():
    return "Olá, Matheus"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Olá, {name}"