from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá, Mundo!"

@app.route("/matheus")
def matheus():
    return "Olá, Matheus"