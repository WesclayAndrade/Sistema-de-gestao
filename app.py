import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def obter_conexao():
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_banco = os.path.join(pasta_atual, "teste1.db")

    conexao = sqlite3.connect(caminho_banco)
    conexao.row_factory = sqlite3.Row #acessa as colunas 
    return conexao

@app.route("/", methods=["GET"]) # lê os dados do banco e entrega na tela 
def pagina_inicial():
    conexao = obter_conexao()
#buscando o cadastro para preencher 
    cadastro = conexao.execute("SELECT * FROM cadastro;").fetchall()
#buscar em produtos 
    consulta_produtos = """
        SELECT produtos.id, produtos.nome, produtos.valor, cadastro.nome AS cadastro_nome
        FROM produtos
        LEFT JOIN cadastro ON produtos.cadastro_id = cadastro.id;
        """
    produtos = conexao.execute(consulta_produtos).fetchall()
    conexao.close()

    return render_template("index.html", lista_cadastro=cadastro, lista_produtos=produtos)

@app.route("/adicionar-produtos", methods=["POST"]) #fazer o cadastro de produtos
def adicionar_produto():
    print("DADOS ENVIADOS", request.form)
    #capturar o valor do input com name="nome_produto"
    nome = request.form.get("nome_produto")
    valor = request.form.get("valor")
    tipo = request.form.get("tipo")
    cadastro_id = request.form.get("cadastro")


    if nome and valor and tipo and cadastro_id :
        conexao = obter_conexao()
        conexao.execute("INSERT INTO produtos (nome, valor, tipo, cadastro_id) VALUES (?,?,?,?);",
                        (nome, float(valor), tipo, int(cadastro_id) ))
        conexao.commit()
        conexao.close()

    return redirect(url_for("pagina_inicial")) #redireciona o navegador para página inicial


@app.route("/adicionar-cadastro", methods=["POST"])
def adicionar_cadastro(): #fazer o cadastro de clientes
    nome = request.form.get("nome")
    telefone = request.form.get("Telefone")
    endereco = request.form.get("Endereço")

    if nome and telefone and endereco:
        conexao = obter_conexao()
        conexao.execute(
            "INSERT INTO cadastro (nome, telefone, endereco) VALUES (?,?,?);",
            (nome, telefone, endereco)
        )
        conexao.commit()
        conexao.close()

    return redirect(url_for("pagina_inicial"))

@app.route("/excluir-produto/<int:produto_id>", methods=["POST"])
def excluir_produto(produto_id):
    conexao = obter_conexao()
    conexao.execute("DELETE FROM produtos WHERE id = ?;", (produto_id,))
    conexao.commit()
    conexao.close()
    return redirect(url_for("pagina_inicial"))

if __name__ == "__main__":
    app.run(debug=True)
    