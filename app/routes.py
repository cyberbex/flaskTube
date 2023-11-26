from flask import render_template, request

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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    return "usuarios: {} e senha: {}".format(usuario,senha)