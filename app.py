from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá, Mundo!"

@app.route("/matheus")
def matheus():
    return "Olá, Matheus"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Olá, {name}"