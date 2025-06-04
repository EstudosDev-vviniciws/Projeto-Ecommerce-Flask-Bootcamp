from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page_home():
    return render_template("home.html")

@app.route('/produtos')
def page_produto():
    itens = [
        {'id': 1, 'nome': 'Celular', 'cod_barra': '34252525313', 'preco': 1200},
        {'id': 2, 'nome': 'Headseat', 'cod_barra': '3124124562', 'preco': 350},
        {'id': 3, 'nome': 'Monitor', 'cod_barra': '647462743618', 'preco': 1450},
        {'id': 4, 'nome': 'Teclado', 'cod_barra': '345836732563', 'preco': 450},
        {'id': 5, 'nome': 'Cadeira', 'cod_barra': '797695834252', 'preco': 670}
    ]
    return render_template("produtos.html", itens=itens)