from flask import render_template

from app import app


@app.route('/')
@app.route('/',defaults={"nome":"usuario","telefone":"4565464","email":"gamba@ds.com"})
@app.route('/index',defaults={"nome":"usuario","telefone":"4565464","email":"gamba@ds.com"})
@app.route('/index/<nome>/<telefone>/<email>')

def index(nome,telefone,email):
    
    dados= { "Nome":"bruno", "Telefone":telefone,"Email":email }
    return render_template('index.html', nome = nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')