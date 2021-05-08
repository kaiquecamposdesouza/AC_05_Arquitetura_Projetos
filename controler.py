from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
from DB import Inserir, Seleciona
import os

insert = Inserir()
select = Seleciona()

app = Flask(__name__)
app.secret_key = "SISPET"

class Estoque():
    def __init__(self, id, produto, categoria, valor, quantidade, descricao):
        self.id = id 
        self.produto = produto
        self.categoria = categoria
        self.valor = valor
        self.quantidade = quantidade
        self.descricao = descricao

@app.route('/')
def cadastra_estoque():
    objetos_estoque = []
    lista = []
    start = select.start()
    lista = select.selec_estoque(start)
    for item in lista:
        estoque = Estoque(item[0], item[1], item[2], item[3], item[4], item[5])
        objetos_estoque.append(estoque)
    return render_template('estoque.html', titulo='Estoque', lista=objetos_estoque)

@app.route('/autentica_estoque_ac05', methods=['POST',])
def cria_estoque():
    produto = request.form['produto']
    print(produto)
    categoria = request.form['categoria']
    valor = float(request.form['valor'])
    quantidade = int(request.form['quantidade'])
    descricao = request.form['descricao']

    start = insert.start()
    insert.inseri_dados_estoque(produto, categoria, valor, quantidade, descricao, start)
    return redirect(url_for('cadastra_estoque'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host='127.0.0.1', port=port)