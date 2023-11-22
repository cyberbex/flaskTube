from flask import render_template

from app import app


@app.route('/')
@app.route('/index')

def index():
    nome = 'bruno'
    dados= { "Nome":"bruno", "Telefone":34534345,"Email":"cyberbex@gmail" }
    return render_template('index.html', nome = nome, dados=dados)

