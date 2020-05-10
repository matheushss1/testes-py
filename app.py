import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    headline= "Olá, Mundo"
    return render_template("index.html", headline= headline)

@app.route("/bye")
def bye():
    headline= "Adeus, Mundo"
    return render_template("index.html", headline= headline)


@app.route("/matheus")
def matheus():
    return "Olá, Matheus"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Olá, {name}"

@app.route("/meuniver")
def niver():
    now = datetime.datetime.now()
    niver = now.month == 6 and now.day == 20
    return render_template("niver.html", niver=niver)

@app.route("/nome_completo")
def nome():
    nomes = ["Matheus", "Henrique", "de", "Souza", "Silva"]
    return render_template("nome_completo.html", nomes=nomes)

@app.route("/apresentacao", methods=["POST"])
def apresentacao():
    nome = request.form.get("nome")
    return render_template("apresentacao.html", nome=nome)