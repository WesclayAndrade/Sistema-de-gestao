import os 
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def obter_conexao():
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_banco = os.path.join(pasta_atual, "BDcompra.db")

    conexao = sqlite3.connect(caminho_banco)
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route("/", methods=["GET"])
def pagina_incial():
    conexao = obter_conexao()

    cadastro = conexao.execute("SELECT id, nome FROM cadastro;").fetchall()

    produto = conexao.execute("SELECT id, tipo_produto, valor_produto FROM produto;").fetchall()

    consulta_produto = """
        SELECT 
            venda.id AS venda_id,
            produto.tipo_produto AS cliente_nome,
            produto.valor_produto AS produto_valor,
            venda.data_venda
            From venda
            INNER JOIN cadastro ON venda.cadastro_id = cadastro.id
            INNER JOIN produto ON venda.produto_id = produto.id
            ORDER BY venda.id DESC;
    """

    venda = conexao.execute(consulta_produto).fetchall()
    conexao.close()

    return render_template(
        "index.html",
        cliente=cliente,
        produto=produto,
        venda=venda
    )

if __name__ == "__main__":
    app.run(debug=True)
